# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class salon_de__couture(models.Model):
    _name = 'salon_de__couture.salon_de__couture'
    _inherit = "res.partner"
    name = fields.Char('Option')
    
    

    nom = fields.Many2one('res.partner',String='nom')
    prenom = fields.Char(string='Prenom', required=True)
    age = fields.Char(string='Age', readonly=True, store=True)
    date_de_naissance = fields.Date(string='Date de naissance', required=True)
    specialite = fields.Selection([('homme', 'homme'),('femme', 'femme'),('enfant', 'enfant'),],'Specialite', default='homme')
    contact = fields.Char('Contact ')
    claude = fields.One2many(comodel_name="mesure.mesure", inverse_name="liaison_client",string="Vos clients")
    nb_mesure = fields.Integer(compute='_nb_mesure')


    @api.model_create_single
    def create(self, vals):
        _logger.error(vals)
        return super(salon_de__couture, self).create(vals)

    @api.onchange ('date_de_naissance')
    def set_age(self):
        for rec in self:
            if rec.date_de_naissance:
                dt = rec.date_de_naissance
                d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + ' Ans'


    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    @api.multi
    def _nb_mesure (self):
        for each in self:
            mesure_ids = self.env['mesure.mesure'].search([('create_uid','=',each.user_account.id)])
            if mesure_ids:
                each.nb_mesure = lent(mesure_ids)
