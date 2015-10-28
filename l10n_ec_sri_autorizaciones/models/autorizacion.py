# -*- coding: utf-8 -*-
from openerp import models, fields

class Autorizacion(models.Model):
    name = 'l10n_ec_sri_autorizaciones.autorizacion'
    description = 'Autorizaciones de comprobantes SRI'
    
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
    lineaautorizacion = fields.One2many('l10n_ec_sri_autorizaciones.autorizacion',
                              inverse_name='autorizacion_id',
                              ondelete='set null',
                              string="Comprobantes autorizados")

class LineaAutorizacion(models.Model):
    name = 'l10n_ec_sri_autorizaciones.lineaautorizacion'
    description = 'Comprobantes Autorizados'
    
    comprobante_id = fields.Many2one('l10n_ec_sri_ats_16.comprobante',
        ondelete='set null', string="Comprobante", required=True)
    secuencia_inicial = fields.Char('Secuencia inicial')
    secuencia_final = fields.Char('Secuencia final')
    secuencia_siguiente = fields.Char('Secuencia siguiente',
                                      help='Ingrese el número de documento que continua en la secuencia',
                                      required=True)
    autorizacion_id = fields.Many2one('l10n_ec_sri_autorizaciones.autorizacion',
                            string='Autorización')
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: