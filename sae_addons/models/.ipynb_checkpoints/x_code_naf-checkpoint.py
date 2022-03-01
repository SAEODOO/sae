# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class CodeNaf(models.Model):
    _inherit = 'x_code_naf'
    _rec_name = 'x_studio_code'
    
    def name_get(self):
    result = []
    for rec in self:
        if rec.x_studio_code:
            result.append((rec.id, rec.x_studio_code))
    return result