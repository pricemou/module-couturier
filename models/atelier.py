# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Ftelier(models.Model):
    _name = 'atelier.atelier'
    _rec_name = 'client'

    client = fields.Char('Voir ')
    liaison_client = fields.One2many(comodel_name="mesure.mesure", inverse_name="liaison_client",string="Vos clients")
    liste = fields.Text('Contact ')
    voir = fields.Text('Voir ')
    
 