# -*- coding: utf-8 -*-
from openerp import models, fields

class Persona(models.Model):
    name = 'l10n_ec_sri_ats_16.persona'
    description = 'Tipo Persona SRI'
    
    name = fields.Char('Tipo de persona')
    code = fields.Char('Código', size='1')
    
class Comprobante(models.Model):
    name = 'l10n_ec_sri_ats_16.comprobante'
    description = 'Comprobantes Autorizados'
    
    name = fields.Char('Comprobante')
    code = fields.Char('Código', size='2')
    sustento_ids = fields.Many2many('l10n_ec_sri_ats_16.sustento',
                                    'sustento_comprobante_relacion',
                                    'comprobante_ids',
                                    'sustento_ids',
                                    string="Sustentos aplicables")
    
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
    comprobante_ids = fields.Many2many('l10n_ec_sri_ats_16.comprobante',
                                       'sustento_comprobante_relacion',
                                       'sustento_ids',
                                       'comprobante_ids',
                                       string="Comprobantes",
                                       help="Seleccione los comprobantes con los cuales es posible utilizar el presente sustento tributario.")
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: