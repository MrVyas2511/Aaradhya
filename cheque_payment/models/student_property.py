from odoo import api,models,fields

class StudentProperty(models.Model):
    _inherit = ['student.property']

    cheque_ids = fields.One2many('cheque.property', 'student_id')
