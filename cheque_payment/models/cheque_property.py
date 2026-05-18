from odoo import api,models,fields

class ChequeProperty(models.Model):
    _name = "cheque.property"
    _description = "Test Model"
    _inherit = ['mail.thread']

    name = fields.Char('Title',required=True)
    student_id = fields.Many2one('student.property', string="Students")
    cheque_no = fields.Char('Cheque Number', required=True)
    bank_name_id = fields.Many2one('bank.name')
    cheque_amount = fields.Float('Amount', default=0.0)
    due_date = fields.Date('Available from',copy=False,default= fields.Date.add(fields.date.today()))
    state = fields.Selection(
                selection =[
                            ('draft','Draft'), 
                            ('ready_to_submit','Ready to Submit'),
                            ('submitted','Submitted'),
                            ('cleared','Cleared')],
                tracking=True, default='draft')
    description = fields.Char()
    due_today_color = fields.Boolean(compute="_compute_due_today_color", store=True)

    @api.depends('due_date')
    def _compute_due_today_color(self):
        for rec in self:
            rec.due_today_color = False
            if rec.due_date == fields.Date.today():
                rec.due_today_color = True