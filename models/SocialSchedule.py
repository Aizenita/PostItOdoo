from odoo import fields, models


class SocialSchedule(models.Model):
    _name = 'postitodoo.socialschedule'
    _description = 'Maneja publicaciones programadas'

    post_id = fields.Many2one('postitodoo.socialpost', string='Publicación programada', required=True)
    scheduled_time = fields.Datetime(string='Fecha y hora de publicación', required=True)
    status = fields.Selection([
        ('scheduled', 'Programada'),
        ('published', 'Publicada'),
        ('pending', 'Pendiente'),
        ('failed', 'Fallida')
    ], string='Estado', default='pending', required=True)
