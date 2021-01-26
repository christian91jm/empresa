from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime

class facturas_model(models.Model):
    _name = 'empresa.facturas_model'
    _description = 'modelo de facturas'
    _sql_constraints = [('facturas_name_uniq','UNIQUE (name)','No puede haber dos facturas con el mismo identificador'),]
    
    ref = fields.Char(string="Referencia", required=True)
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    cliente = fields.Many2many("empresa.clientes.model", string="Cliente")
    detallef = fields.One2many("empresa.detfac_model", "facturas_id", string="Factura")
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('7','7'),('5','5'),('0','0')])
    total = fields.Float(string="Total", compute="_calc_iva", store=True)

    @api.depends('detallef')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.detallef:
            suma+= i.productos_id.pvp*i.cantidad
        self.base=suma

    @api.depends('iva','base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = ((self.base*int(self.iva))/100)+self.base



    
