# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos_model(models.Model):
    _name = 'empresa.productos_model'
    _description = 'empresa.productos_model'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Html(string="Descripcion", required=True)
    pvp = fields.Float(string="PVP", default=0 , required=True)
    cantidad = fields.Integer(string="Cantidad", default=1, required=True )
    detallef = fields.One2many("empresa.detfac_model","productos_id","Facturas")