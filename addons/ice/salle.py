# -*- coding: utf-8 -*-
from odoo import models, fields

class Salle(models.Model):
    _name = 'gestionp_salle'
    _description = 'Salle de classe'

    name = fields.Char(string='Nom de la salle', required=True)
    capacite = fields.Integer(string='Capacité')
    enseignant_id = fields.One2many('gestionp_enseignant', 'salle_id', string='Enseignant')
    eleve_ids = fields.One2many('gestionp_eleve', 'salle_id', string='Élèves')