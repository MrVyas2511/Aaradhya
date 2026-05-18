from odoo import api,models,fields

class StudentProperty(models.Model):
    _name = "student.class"
    _description = "Standard"

    name = fields.Char('Title',required=True)