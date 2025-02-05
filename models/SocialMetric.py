from odoo import fields, models, api


class SocialMetric(models.Model):
    _name = 'postitodoo.socialmetric'
    _description = 'Métricas de red social'

    likes = fields.Integer(string='Likes', default=0)
    comments = fields.Integer(string='Comentarios', default=0)
    shares = fields.Integer(string='Compartidos', default=0)
    impressions = fields.Integer(string='Vistas', default=0)
    date = fields.Datetime(string='Fecha de la métrica', required=True)

    # Relación con Publicaciones
    post_id = fields.Many2one('postitodoo.socialpost', string='Publicación asociada', required=True)

    # Campo calculado para engagement rate
    engagement = fields.Float(string='Nivel de interacción', compute='_compute_engagement', store=True)

    @api.depends('likes', 'impressions')
    def _compute_engagement(self):
        for record in self:
            record.engagement = (record.likes / record.impressions * 100) if record.impressions else 0
