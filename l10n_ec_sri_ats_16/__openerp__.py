# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Ecuador - SRI - Anexo Transaccional",
    "version" : "1.0",
    "author" : "Comunidad Odoo Ecuador",
    'website' : '',
    "category" : "Localization/Account Charts",
    "description": """
SRI - Anexo transaccional.
============================================

    * Se crean los modelos requeridos para generar el ATS.
        * Tipos de comprobante.
        * Sustentos tributarios.
        * Tipos de documento de identificación.
        * Tipos de persona.
    * Se definen características especiales para el res.partner a través de su posición fiscal.
        * Tipo de documento.
        * Tipo de persona.

""",
    'depends' : ['account',
                 'l10n_ec_sri_16',
                 ],
    'data' : [
        'views/ats_views.xml',
        'views/partner_views.xml',
        'views/account_tax_views.xml',
        'views/fiscal_position_views.xml',
        "data/l10n_ec_sri_16.sustento.csv",
        ],
    'demo': [],
    'auto_install': False,
    'installable': True,
    'images': [],
}
