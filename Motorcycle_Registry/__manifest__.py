{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': ''''Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
        ''',
    'author': 'jopi-odoo',
    'website': 'https://github.com/jopi-odoo/technical_training',
    'category': 'Kawiil/Kawiil',
    'depends': ['stock',],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml',
        'data/registry_data.xml',
        'views/motorcycle_registry_menulist.xml',
        'views/motorcycle_registry_view.xml',
        'views/product_view_inherit.xml',
    ],
    'demo': [
        'demo/registry_demo.xml', 
    ],
    'application': True,
}