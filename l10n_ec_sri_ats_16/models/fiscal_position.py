# -*- coding: utf-8 -*-
from openerp import models, fields

class FiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'
    
    documento_id = fields.Many2one('l10n_ec_sri_ats_16.documento', ondelete='set null', string="Tipo de documento")
    persona_id = fields.Many2one('l10n_ec_sri_ats_16.persona', ondelete='set null', string="Tipo de persona")