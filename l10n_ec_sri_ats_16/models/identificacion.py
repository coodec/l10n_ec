# -*- coding: utf-8 -*-
from openerp import models, fields
    
class Identificacion(models.Model):
    _name = 'l10n_ec_sri_ats_16.identificacion'
    
    name = fields.Char('Tipo de identificacion')
    code = fields.Char('Código', size=2)
    active = fields.Boolean('Activo')
    description = fields.Char('Descripción')
    ats_compras = fields.Char('Código en compras', size=2)
    ats_ventas = fields.Char('Código en ventas', size=2)
    id_proveedor = fields.Char('Código en proveedor', size=2)