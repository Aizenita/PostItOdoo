from odoo import fields, models


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
