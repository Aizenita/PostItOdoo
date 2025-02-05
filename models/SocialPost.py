import base64
import tempfile

from custom_addons.postitodoo.MetaClient import MetaClient
from odoo import api,fields, models
from odoo.exceptions import UserError


class SocialPost(models.Model):
    _name = 'postitodoo.socialpost'
    _description = 'Publicaciones de red social'

    name = fields.Char(string='Título de la publicación', required=True)
    content = fields.Text(string='Contenido', required=True)
    image = fields.Binary(string='Imagen')
    post_date = fields.Datetime(string='Fecha de publicación', required=True)

    status = fields.Selection([
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
        ('queued', 'Programado'),
        ('failed', 'Fallido')
    ], string='Estado', default='draft', required=True)

    # Relaciones
    account_id = fields.Many2one('postitodoo.socialaccount', string='Cuenta asociada', required=True)
    metric_ids = fields.One2many('postitodoo.socialmetric', 'post_id', string='Métricas de la publicación')
    campaign_id = fields.Many2one('postitodoo.socialcampaign', string='Campaña asociada')
    hashtag_ids = fields.Many2many('postitodoo.socialhashtag', string='Hashtags utilizados')

    def action_post_facebook(self):
        """Ejemplo de acción para publicar en Facebook."""
        self.ensure_one()  # Para trabajar solo con un registro a la vez

        # Verificamos que la cuenta tenga token y page_id
        if not self.account_id.access_token or not self.account_id.page_id:
            raise UserError("La cuenta asociada no tiene configurado el Token o el Page ID.")

        # Creamos la instancia del cliente
        client = MetaClient(self.account_id.page_id, self.account_id.access_token)

        # Si hay imagen, la publicamos como foto; si no, publicamos solo el texto
        if self.image:
            # Decodificamos el base64 y lo volcamos a un archivo temporal
            image_data = base64.b64decode(self.image)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                tmp.write(image_data)
                tmp.flush()
                tmp_path = tmp.name

            # Llamada a la API para subir la imagen + mensaje
            response = client.post_image_Facebook(tmp_path, self.content)

        else:
            # Llamada a la API para subir solo el texto
            response = client.post_message_Facebook(self.content)

        # Manejo de la respuesta
        if response.status_code == 200:
            # Normalmente Facebook devuelve un JSON con el ID de la publicación
            data = response.json()
            post_id = data.get("id")
            if post_id:
                # Podrías guardar la referencia en algún campo si deseas
                # Por ejemplo, self.fb_post_id = post_id
                self.status = 'published'
            else:
                self.status = 'failed'
                raise UserError("Se publicó, pero no se recibió el ID de la publicación.")
        else:
            # Si hubo error, marcamos el estado como fallido y levantamos excepción
            self.status = 'failed'
            error_msg = response.json().get("error", {}).get("message", "Error desconocido")
            raise UserError(f"Error al publicar en Facebook: {error_msg}")

    @api.model
    def cron_post_queued_posts(self):
        """Se ejecuta periódicamente para publicar los posts en estado 'queued'
           cuya fecha de publicación ya llegó."""
        # 1) Buscar publicaciones en estado 'queued' con 'post_date' <= fecha/hora actual
        now = fields.Datetime.now()
        queued_posts = self.search([
            ('status', '=', 'queued'),
            ('post_date', '<=', now)
        ])
        # 2) Para cada publicación, llamar a la acción de publicación
        for post in queued_posts:
            # Manejar excepción si algo falla, para que el resto de posts continúen
            try:
                post.action_post_facebook()
            except Exception as e:
                post.status = 'failed'  # O registrar log del error
