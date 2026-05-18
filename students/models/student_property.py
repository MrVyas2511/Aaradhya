from odoo import api,models,fields

class StudentProperty(models.Model):
    _name = "student.property"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Title',required=True)
    description = fields.Char()
    standard = fields.Many2one('student.class', required=True)
    parent_contact = fields.Char('Parent Contact No.', required=True)
    alternative_contact = fields.Char('Alternative No')
    dob = fields.Date('D.O.B.')
    gender = fields.Selection([("male", "Male"), ("female", "Female")])
    medium = fields.Selection([("gujarati", "Gujarati"), ("english", "English")], required=True, default="gujarati")
    batch = fields.Many2one('student.batch', required=True)
    subject = fields.Char()

    @api.model    
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        if not self.env.user.has_group("base.group_system"):
            domain.append(('standard', 'in', self.env.user.batch_id.ids))
        return super()._search(domain=domain, offset=offset, limit=limit, order=order, access_rights_uid=access_rights_uid)
    