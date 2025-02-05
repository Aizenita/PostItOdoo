from odoo import fields, models


class SocialAccount(models.Model):
    _name = 'postitodoo.socialaccount'
    _description = 'Cuenta de red social'

    name = fields.Char(string='Nombre de la cuenta', required=True)
    platform = fields.Selection([
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp')
    ], string='Plataforma', default='facebook', required=True)
    api_key = fields.Char(string='Clave API', help="Clave para la integración con la plataforma")
    is_active = fields.Boolean(string='Activo', default=True)

    # Relación One2many con SocialPost
    post_ids = fields.One2many('postitodoo.socialpost', 'account_id', string='Publicaciones asociadas')
