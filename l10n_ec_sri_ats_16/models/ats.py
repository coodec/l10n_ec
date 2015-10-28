# -*- coding: utf-8 -*-
from openerp import models, fields

class Persona(models.Model):
    _name = 'l10n_ec_sri_ats_16.persona'

    name = fields.Char('Tipo de persona')
    code = fields.Char('Código', size=1)
    active = fields.Boolean('Activo')
    
class Comprobante(models.Model):
    _name = 'l10n_ec_sri_ats_16.comprobante'
    
    name = fields.Char('Comprobantes autorizados')
    code = fields.Char('Código', size=2)
    active = fields.Boolean('Activo')
    sustento_ids = fields.Many2many('l10n_ec_sri_ats_16.sustento',
                                    'sustento_comprobante_relacion',
                                    'comprobante_ids',
                                    'sustento_ids',
                                    string="Sustentos aplicables")
    
class Identificacion(models.Model):
    _name = 'l10n_ec_sri_ats_16.identificacion'
    
    name = fields.Char('Tipo de identificacion')
    code = fields.Char('Código', size=2)
    active = fields.Boolean('Activo')
    description = fields.Char('Descripción')
    ats_compras = fields.Char('Código en compras', size=2)
    ats_ventas = fields.Char('Código en ventas', size=2)
    id_proveedor = fields.Char('Código en proveedor', size=2)

class Sustento(models.Model):
    _name = 'l10n_ec_sri_ats_16.sustento'
    
    name = fields.Char('Sustento Tributario')
    code = fields.Char('Código', size=2)
    active = fields.Boolean('Activo')
    description = fields.Char('Descripción')
    comprobante_ids = fields.Many2many('l10n_ec_sri_ats_16.comprobante',
                                       'sustento_comprobante_relacion',
                                       'sustento_ids',
                                       'comprobante_ids',
                                       string="Comprobantes",
                                       help="Seleccione los comprobantes con los cuales es posible utilizar el presente sustento tributario.")