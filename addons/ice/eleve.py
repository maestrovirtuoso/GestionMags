# -*- coding: utf-8 -*-
from odoo import models, fields

class Eleve(models.Model):
    _name = "gestionp_eleve"
    _description = 'Élève'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    enseignant_id = fields.Many2one('gestionp_enseignant', string='Enseignant')
    salle_id = fields.Many2one('gestionp_salle', string='Salle de classe')