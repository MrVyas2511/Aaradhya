from odoo import api,models,fields

class StudentProperty(models.Model):
    _name = "bank.name"

    name = fields.Char("Bank Name")