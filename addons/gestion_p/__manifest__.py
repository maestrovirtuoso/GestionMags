# -*- coding: utf-8 -*-
{
    'name': "gestionP",

    'summary': "Nous realisons une simple application de suivie des activites d'un magasin",

    'description': """
Long description of module's purpose
je suis entrain de faire un travail pour nasara
    """,

    'author': "Uriel enterprise",
    'website': "urielakam2@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Formation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
          
        'security/ir.model.access.csv',
        'views/category_views.xml',
        'views/product_views.xml',
        'views/user_views.xml',
        'views/menu_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

