# -*- coding: utf-8 -*-
from odoo import models, fields

class Enseignant(models.Model):
    _name = 'gestionp_enseignant'
    _description = 'Enseignant'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    salle_id = fields.Many2one('gestionp_salle', string='Salle de classe')
    eleve_ids = fields.One2many('gestionp_eleve', 'enseignant_id', string='Élèves')