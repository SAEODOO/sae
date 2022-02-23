# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    test = fields.Char('TEst')

    def _action_confirm(self):
        for rec in self:
            product_ids = set(self.order_line.mapped('product_id.id'))
            delivery_ids = set(self.env['delivery.carrier'].search([]).mapped('product_id.id'))
            if not product_ids.intersection(delivery_ids):
                from odoo.exceptions import ValidationError(_('Please add a delivery service before confirming the order.'))
        res = super(SaleOrder, self)._action_confirm()
