# -*- coding: utf-8 -*-
# from odoo import http


# class SaeAddons(http.Controller):
#     @http.route('/sae_addons/sae_addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sae_addons/sae_addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sae_addons.listing', {
#             'root': '/sae_addons/sae_addons',
#             'objects': http.request.env['sae_addons.sae_addons'].search([]),
#         })

#     @http.route('/sae_addons/sae_addons/objects/<model("sae_addons.sae_addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sae_addons.object', {
#             'object': obj
#         })
