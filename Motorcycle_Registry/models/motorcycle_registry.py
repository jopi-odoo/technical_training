from odoo import api, fields, models
from odoo.exceptions import ValidationError

import re

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


    _sql_constraints = [('unique_vin', 'unique(vin)', 'The VIN must be unique.'),]


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)


    @api.constrains('vin')
    def _check_vin(self):
        vin_pattern = r'^[A-Z]{4}\d{2}[A-Z\d]{2}\d{6}$'
        for registry_number in self:
            if re.match(vin_pattern, registry_number.vin) == None:
                raise ValidationError("""The VIN must follow the pattern \n
                                      Make - 2 Capital Letters \n
                                      Model - 2 Capital Letters \n
                                      Year - 2 Digits \n
                                      Battery Capacity - 2 Capital Letters or Numbers \n
                                      Serial Number - 6 Digits """)

    
    @api.constrains('license_plate')
    def _check_license_plate(self):
        license_plate_pattern = r'^[A-Z]{1,4}\d{1,3}(?:[A-Z]{2})?$'
        for registry_number in self:
            if re.match(license_plate_pattern, registry_number.license_plate) == None:
                raise ValidationError("""The License Plate must follow the pattern \n
                                      1-4 Capital Letters \n
                                      1-3 Digits \n
                                      Optional 2 Capital Letters """)
            