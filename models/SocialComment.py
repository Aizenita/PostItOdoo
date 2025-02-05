from odoo import fields, models


class SocialComment(models.Model):
    _name = 'postitodoo.socialcomment'
    _description = 'Analiza interacciones de comentarios'

    post_id = fields.Many2one('postitodoo.socialpost', string='Publicación asociada', required=True)
    author = fields.Char(string='Autor', required=True)
    content = fields.Text(string='Contenido', required=True)
    date = fields.Datetime(string='Fecha y hora', required=True)
