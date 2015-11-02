# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    tradename = fields.Char('Nombre Comercial', size=300)
            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
