# -*- coding: utf-8 -*-
from odoo import models, fields

class User(models.Model):
    _name = 'gestionp_user'
    _description = 'Utilisateur de la boutique'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    username = fields.Char(string='Username', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    email = fields.Char(string='Email')  # Corrigé : "Char" avec majuscule
    password = fields.Char(string='Mot de passe', required=True)
    city = fields.Char(string='Quartier')