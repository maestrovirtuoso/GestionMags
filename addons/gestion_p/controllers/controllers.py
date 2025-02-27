# -*- coding: utf-8 -*-
# from odoo import http


# class GestionP(http.Controller):
#     @http.route('/gestion_p/gestion_p', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_p/gestion_p/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_p.listing', {
#             'root': '/gestion_p/gestion_p',
#             'objects': http.request.env['gestion_p.gestion_p'].search([]),
#         })

#     @http.route('/gestion_p/gestion_p/objects/<model("gestion_p.gestion_p"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_p.object', {
#             'object': obj
#         })

