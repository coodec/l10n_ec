# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Ecuador - Niif Pymes - Base",
    "version" : "1.0",
    "author" : "Comunidad Odoo Ecuador",
    'website' : '',
    "category" : "Localization/Account Charts",
    "description": """
Cuentas contables comunes para NIIF Pymes.
===============================================

    * Plan de Cuentas base.
        * Se asume que usted no ha creado cuentas contables anteriores, si lo ha hecho, deberá eliminarlas o modificarlas de manera manual.
        * Se asume que no existen cuentas contables creadas, por lo que el "external id" de la cuenta raíz será "__export__.account.account_1".
        * Utiliza únicamente cuentas contables existentes en el plan de cuentas Niif que ha publicado la Superintendencia de Compañías del Ecuador.
        * Se eliminan cuentas contables poco usadadas o requeridas en insdustrias específicas como la construcción.
        * El módulo crea solamente una cuenta contable a través de la plantilla (Raiz), sin embargo, el resto de cuentas son escritas directamente a la base de datos a fin de poder controlar el "external id" de cada cuenta, permitiendo su posterior manipulación a través de código.        

IMPORTANTE: Este módulo no funciona como una plantilla normal de Odoo, registra sus componentes directamente en la empresa matriz de la base de datos. 

Si desea una plantilla debe editar el código acorde a los modelos estandar, puede usar como ejemplo el módulo l10n_lu o l10n_si.

Usar una plantilla solo es necesario cuando desea usar el sistema en un entorno multi-compañías, caso contrario, este módulo le será útil tal y como ha sido desarrollado.
""",
    'depends' : ["account"],
    'data' : [
        'data/account_chart.xml',
        'data/account.account.csv',
        ],
    'demo': [],
    'auto_install': False,
    'installable': True,
    'images': [],
}
