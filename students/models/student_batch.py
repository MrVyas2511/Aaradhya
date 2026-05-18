from odoo import api,models,fields

class StudentProperty(models.Model):
    _name = "student.batch"
    _description = "Batch"

    name = fields.Char('Title',required=True)