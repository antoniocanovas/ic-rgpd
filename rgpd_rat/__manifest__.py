# -*- coding: utf-8 -*-

{
    'name': "rgpd_rat",

    'summary': """
        Modulo para gestionar los rat's RGPD """,

    'description': """
       *****
    """,

    'author': "Pedro Guirao",
    'website': "https://ingenieriacloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','project','base_automation','hr'],

    # always loaded
    'data': [
        'views/x_partner_view.xml',
        'views/server_actions.xml',
        'views/views.xml',
        'demo/demo.xml',
        'demo/data_opciones.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}
