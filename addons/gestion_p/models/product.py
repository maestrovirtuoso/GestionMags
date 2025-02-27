# -*- coding: utf-8 -*-
from odoo import models, fields

class Product(models.Model):
    _name = 'gestionp_product'
    _description = 'Produit de la boutique'

    name = fields.Char(string='Nom du produit', required=True)
    category_id = fields.Many2one('gestionp_category', string='Catégorie')  # ⚠️ Ce champ doit correspondre à l'`inverse_name` dans `gestionp_category`
    description = fields.Text(string='Description du produit')
    image = fields.Binary(string='Image du produit')
    prix = fields.Float(string='Prix du produit', digits=(6, 2), required=True)