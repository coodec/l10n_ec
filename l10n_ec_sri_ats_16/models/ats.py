# -*- coding: utf-8 -*-
from openerp import models, fields

class Persona(models.Model):
    name = 'l10n_ec_sri_ats_16.persona'
    description = 'Tipo Persona SRI'
    
    name = fields.Char('Tipo de persona')
    code = fields.Char('Código', size='1')

class Identificacion(models.Model):
    name = 'l10n_ec_sri_ats_16.identificacion'
    description = 'Tipo de Identificación'
    
    name = fields.Char('Tipo de identificación')
    code = fields.Char('Código', size='2')
    description = fields.Char('Descripción')
    ats_compras = fields.Char('Código en compras', size='2')
    ats_ventas = fields.Char('Código en ventas', size='2')
    
class Sustento(models.Model):
    name = 'l10n_ec_sri_ats_16.sustento'
    description = 'Tipo Sustento SRI'
    
    name = fields.Char('Sustento Tributario')
    code = fields.Char('Código', size='2')
    description = fields.Char('Descripción')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: