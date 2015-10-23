# -*- coding: utf-8 -*-
{
    'name': "Agrega el Nombre comercial",

    'summary': """Agrega la posibiliad de agragar el nombre comercial""",

    'description': """
Agrega el nombre comercial
=============================================
    * Modificaciones en res.partner.
        * Agrega el campo tradename en res.partner.
        * Agrega el campo tradename en la vista de res.partner.
    """,

    'author': 'Comunidad de Odoo Ecuador',
    'website': '',

    'category': 'Tools',
    'version': '0.02',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded 
    'data': [
        'views/partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
