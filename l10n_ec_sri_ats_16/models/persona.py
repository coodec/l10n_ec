# -*- coding: utf-8 -*-
from openerp import models, fields

class Persona(models.Model):
    _name = 'l10n_ec_sri_ats_16.persona'

    name = fields.Char('Tipo de persona')
    code = fields.Char('Código', size=1)
    active = fields.Boolean('Activo')