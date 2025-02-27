from odoo import fields, models, api

class SocialSchedule(models.Model):
    _name = 'postitodoo.socialschedule'
    _description = 'Maneja publicaciones programadas'

    name = fields.Char(
        string='Nombre Programación',
        compute='_compute_name',
        store=True
    )
    post_id = fields.Many2one(
        'postitodoo.socialpost',
        string='Publicación programada',
        required=True
    )
    scheduled_time = fields.Datetime(
        string='Fecha y hora de publicación',
        required=True
    )
    status = fields.Selection([
        ('scheduled', 'Programada'),
        ('published', 'Publicada'),
        ('pending', 'Pendiente'),
        ('failed', 'Fallida')
    ], string='Estado', default='pending', required=True)

    @api.depends('post_id')
    def _compute_name(self):
        """
        Pone en 'name' el título de la publicación.
        Si no hay publicación, muestra un texto por defecto.
        """
        for record in self:
            if record.post_id:
                record.name = record.post_id.name or "Sin título"
            else:
                record.name = "Sin publicación"
