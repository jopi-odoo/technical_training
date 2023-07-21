from odoo import http

class MotorcycleRegistry(http.Controller):
    @http.route('/motorcycle_registry', auth='public', website=True)
    def index(self, **kw):
        return 'Hello world'

    @http.route('/compare', auth='public', website=True)
    def motorcycles(self, **kw):
        motorcycles = http.request.env['product.template'].search([])
        return http.request.render('Motorcycle_Registry.products_website', {
            'motorcycles': motorcycles,
        })