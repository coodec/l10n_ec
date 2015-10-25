# -*- coding: utf-8 -*-
from openerp import models, fields

class Persona(models.Model):
    name = 'l10n_ec_sri_ats_16.persona'
    description = 'Tipo Persona SRI'
    
    name = fields.Char('Tipo de persona')
    code = fields.Char('Código', size='1')

class Documento(models.Model):
    name = 'l10n_ec_sri_ats_16.documento'
    description = 'Tipo Documento SRI'
    
    name = fields.Char('Tipo de documento')
    code = fields.Char('Código', size='2')

class Sustento(models.Model):
    name = 'l10n_ec_sri_ats_16.sustento'
    description = 'Tipo Sustento SRI'
    
    name = fields.Char('Sustento Tributario')
    code = fields.Char('Código', size='2')
    description = fields.Char('Descripción')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: