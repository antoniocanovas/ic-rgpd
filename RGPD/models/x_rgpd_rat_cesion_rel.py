# -*- coding: utf-8 -*-

from odoo import models, fields, api

class x_rgpd_grupo_contacto_rel(models.Model):
    _name= "x_rgpd_rat_cesion_rel"
    _description = "RGPD rel"


    x_name = fields.Char(string="Name")
    x_rat_id = fields.Many2one('x_rgpd_grupos')
    x_cesion_id = fields.Many2one('res.partner')
    x_empresa_id = fields.Many2one('res.partner',related='x_cesion_id.parent_id',stored=False,string='Empresa')