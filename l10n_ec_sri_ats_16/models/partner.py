# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    documento_id = fields.Many2one('l10n_ec_sri_ats_16.documento', ondelete='set null', string="Tipo de documento")
    persona_id = fields.Many2one('l10n_ec_sri_ats_16.persona', ondelete='set null', string="Tipo de persona")
    
    @api.one
    @api.onchange('property_account_position_id')
    def _onchange_property_account_position_id(self):
        if self.property_account_position_id:
            self.documento_id = self.property_account_position_id.documento_id
            self.persona_id = self.property_account_position_id.persona_id
            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
