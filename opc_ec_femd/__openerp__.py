# -*- coding: utf-8 -*-
{
    'name': "Flujo de Efectivo",

    'summary': """Clasificador de pagos y cobros""",

    'description': """
Flujo de Efectivo (directo)
=============================================
    * Modifica account.payment.
        * Agrega los campos para clasificar cobros y pagos.
        * Modifica las vistas necesarias.
    """,

    'author': 'Comunidad de Odoo Ecuador',
    'website': '',

    'category': 'Tools',
    'version': '0.02',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
    ],

    # always loaded 
    'data': [
        'views/payment_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
