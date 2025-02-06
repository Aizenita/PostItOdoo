from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Campos para guardar la API key y otros parámetros
    my_integration_api_key = fields.Char(
        string="API Key",
        config_parameter='my_integration.api_key'
    )
    @api.model
    def get_values(self):
        """Carga los valores de 'ir.config_parameter' para mostrarlos en la vista de ResConfigSettings."""
        res = super().get_values()
        ICPSudo = self.env["ir.config_parameter"].sudo()

        res.update(
            my_integration_api_key=ICPSudo.get_param("my_integration.api_key", default=""),
        )
        return res

    def set_values(self):
        """Guarda los valores introducidos en la vista dentro de 'ir.config_parameter'."""
        super().set_values()
        ICPSudo = self.env["ir.config_parameter"].sudo()
        ICPSudo.set_param("my_integration.api_key", self.my_integration_api_key or "")

    def action_open_my_integration_settings(self):
        """ Método que abre la configuración del módulo en una vista específica """
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Integration Settings',
            'res_model': 'res.config.settings',
            'view_mode': 'form',
            'view_id': self.env.ref('postitodoo.res_config_settings').id,
            'target': 'new',
        }


