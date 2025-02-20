from odoo import fields,models

class SocialCampaign(models.Model):
    _name = 'postitodoo.socialcampaign'
    _description = 'Agrupa publicaciones y analiza su rendimiento en conjunto'

    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha de Fin')
    budget = fields.Float(string='Presupuesto de la campaña')
    status = fields.Selection([
        ('draft', 'Borrador'),
        ('en_curso', 'En Curso'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    ], string='Estado', default='draft')

    # Relación One2many con SocialPost
    post_ids = fields.One2many('postitodoo.socialpost', 'campaign_id', string='Publicaciones de la campaña')

def action_end_campaign(self):

    for campaign in self:
        campaign.status = 'finalizada'