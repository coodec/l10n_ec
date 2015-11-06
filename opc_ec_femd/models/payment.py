# -*- coding: utf-8 -*-
from openerp import models, fields

class Payment(models.Model):
    _inherit = 'account.payment'
    
    cobro_md = fields.Selection([
            ('95010101', 'Cobros procedentes de las ventas de bienes y prestación de servicios'),
            ('95010102', 'Cobros procedentes de regalías, cuotas, comisiones y otros ingresos de actividades ordinarias'),
            ('95010103', 'Cobros procedentes de contratos mantenidos con propósitos de intermediación o para negociar'),
            ('95010104', 'Cobros procedentes de primas y prestaciones, anualidades y otros beneficios de pólizas suscritas'),
            ('95010105', 'Otros cobros por actividades de operación'),
        ], string='Clasificación del cobro', default='95010101')

    pago_md = fields.Selection([
            ('95010201', 'Pagos a proveedores por el suministro de bienes y servicios'),
            ('95010202', 'Pagos procedentes de contratos mantenidos para intermediación o para negociar'),
            ('95010203', 'Pagos a y por cuenta de los empleados'),
            ('95010204', 'Pagos por primas y prestaciones, anualidades y otras obligaciones derivadas de las pólizas suscritas'),
            ('95010205', 'Otros pagos por actividades de operación'),
        ], string='Clasificación del pago', default='95010201')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
