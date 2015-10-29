# -*- coding: utf-8 -*-
from openerp import models, fields

class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    autorizacion_id = fields.Many2one('l10n_ec_sri_autorizaciones.autorizacion',
                                      string='Autorización')