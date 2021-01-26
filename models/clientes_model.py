# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class clientes_model(models.Model):
    _name = 'empresa.clientes_model'
    _description = 'modelo de clientes'

    dni = fields.Char(string="DNI", required=True)
    foto = fields.Binary(string="Foto", required=False)
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Integer(string="Teléfono", required=True, size=9)
    email = fields.Char(string="Email", required=True)
    facturas = fields.One2many("empresa.facturas_model", "cliente", string="Facturas")

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 carácteres!")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")
    
    @api.constrains("email")
    def _validaEmail(self):
        if "@" and "." not in self.email:
            raise ValidationError("Email incorrecto!")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
