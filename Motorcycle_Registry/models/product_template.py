from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], 
                                     ondelete={'motorcycle': 'set product',})

    horsepower = fields.Integer()
    top_speed = fields.Integer()
    torque = fields.Integer()
    battery_capacity = fields.Integer()
    charge_time = fields.Integer()
    range = fields.Integer()
    curb_weight = fields.Integer()
    make = fields.Char()
    model = fields.Char()
    year = fields.Char()

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping

