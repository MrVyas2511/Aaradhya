from odoo import api,models,fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    batch_id = fields.Many2many('student.class', string='Batch')

