# -*- coding: utf-8 -*-
from odoo import models, fields

class Category(models.Model):
    _name = 'gestionp_category'
    _description = 'Catégorie de la boutique'

    name = fields.Char(string='Nom de la catégorie', required=True)
    product_ids = fields.One2many('gestionp_product', 'category_id', string='Produits')  # ⚠️ Le champ 'category_id' doit exister dans 'gestionp_product'