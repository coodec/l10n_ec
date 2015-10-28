# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Autorizacion(models.Model):
    _name = 'l10n_ec_sri_autorizaciones.autorizacion'
    
    autorizacion_propia = fields.Boolean('¿Autorización propia?')
    partner_id = fields.Many2one('res.partner',
                                 string='Cliente/Proveedor',
                                 required=True)
    numero = fields.Integer('Nro. de autorización')
    establecimiento = fields.Char('Establecimiento')
    punto_impresion = fields.Char('Punto de impresión')
    valido_desde = fields.Date('Fecha de emisión',
                          help='Ingrese la fecha en la que la autorización fue emitida por parte del S.R.I.')
    valido_hasta = fields.Date('Fecha de expiración',
                          help='Ingrese la fecha en la que la autorización fue emitida por parte del S.R.I.')
    lineaautorizacion_ids = fields.One2many('l10n_ec_sri_autorizaciones.lineaautorizacion',
                                            inverse_name='autorizacion_id',
                                            ondelete='restrict',
                                            string="Comprobantes autorizados")