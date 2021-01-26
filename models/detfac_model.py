# -*- coding: utf-8 -*-

from odoo import models, fields, api


class detfac_model(models.Model):
    _name = 'empresa.detfac_model'
    _description = 'empresa.detfac_model'

    
    facturas_id = fields.Many2one("empresa.facturas_model", "Factura")
    productos_id = fields.Many2one("empresa.productos_model", "Productos")
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)