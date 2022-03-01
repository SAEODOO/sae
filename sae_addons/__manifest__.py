# -*- coding: utf-8 -*-
{
    'name': "sae_addons",

    'description': """
       SAE Customizations
    """,

    'installable': True,
    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'studio_customization'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
}
