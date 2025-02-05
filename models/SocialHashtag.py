from odoo import fields, models


class SocialHashtag(models.Model):
    _name = 'postitodoo.socialhashtag'
    _description = 'Permite analizar qué hashtags funcionan mejor en qué publicaciones'

    name = fields.Char(string='Hashtag', required=True, help="Ejemplo: #marketing")

    # Relación Many2many con SocialPost
    post_ids = fields.Many2many('postitodoo.socialpost', string='Publicaciones con este hashtag')
