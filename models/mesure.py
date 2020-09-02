# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime

class mesure(models.Model):
    _name = 'mesure.mesure'
    _rec_name = 'autour_poitrine'


    name = fields.Char('Option')

    
    autour_poitrine = fields.Char('Autour poitrine')
    auteur_taille = fields.Char('Auteur taille')
    auteur_des_hanches = fields.Char('Auteur_des_hanches')
    tour_de_poitrine = fields.Char('Tour de poitrine')
    tour_de_taille = fields.Char('Tour de taille')
    tour_de_hancher = fields.Char('Tour de hanche')
    tour_du_bras = fields.Char('Tour du bras')
    longueur_du_bras = fields.Char('Longueur du bras ')
    tour_du_poigner = fields.Char('Tour du poigner')
    hauteur_de_taille = fields.Char('Hauteur de taille')
    photo = fields.Binary(string="Image ",)
    liaison_client = fields.Many2one(string="Client",comodel_name="res.partner")

 