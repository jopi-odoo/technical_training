from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle description'
    _rec_name = 'registry_number'

    registry_number = fields.Char(required=True,
                                    string="Registry Number",
                                    default="MRN0000",
                                    copy=False,
                                    readonly=True)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model
    def created(self, vals):
        if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
            vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals)