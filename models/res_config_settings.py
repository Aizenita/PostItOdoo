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
