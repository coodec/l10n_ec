# -*- coding: utf-8 -*-
###############################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
###############################################

from openerp import models, fields, api

class ConfiguracionesEcuatorianas(models.TransientModel):
    _name = 'l10n_ec_config.config.settings'
    _inherit = 'res.config.settings'

    # Modulos
    module_l10n_ec_ote = fields.Boolean(
        'Instalar la información geopolítica de Ecuador (provincias, cantones, parroquias)',
        help="""Instala el módulo l10n_ec_ote.""")
    module_opc_ec_id_unico = fields.Boolean(
        'Evitar que el número de identificación sea usado en más de una empresa.',
        help="""Instala el módulo opc_ec_id_unico.""")
    module_l10n_ec_sri_2016 = fields.Boolean(
        'Comunes para Pymes en Ecuador (103, 104, ATS).',
        help="""Instala el módulo l10n_ec_2016.""")
    module_l10n_ec_sri_ce_2016 = fields.Boolean(
        'Específicos de empresas que realizan negocios con el exterior.',
        help="""Marcar si su empresa realiza negocios con el exterior y desea registrar las transacciones en el sistema""")
    module_l10n_ec_partner = fields.Boolean(
        'Modificaciones en res_partner.',
        help="""Crea campos adicionales en res_partner.""")
