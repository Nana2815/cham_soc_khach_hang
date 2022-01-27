from odoo import api, models, fields
from odoo.exceptions import ValidationError 
class CustomerCare(models.Model):
    _name = 'customer.care'
    name = fields.Char('Name', required=True)
    phone = fields.Char('Phone number', required=True)
    email = fields.Char('Email', required=True)
    address = fields.Char('Address')
    identity = fields.Char('Identity')
    curator = fields.Char('Curator', readonly=True)
    type = fields.Boolean('Loyal customer', compute="_type", store="true", readonly=True)
    information_line_ids = fields.One2many('customer.care.information.lines','customer_id',string="Information")

    _sql_constraints = [
        ('phone_uniq', 'UNIQUE(phone)', 'Phone number already exists'),
        ('email_uniq', 'UNIQUE(email)', 'Email already exists')
    ]

    @api.model
    def default_get(self, fields_list):
        res = super(CustomerCare, self).default_get(fields_list)
        res["name"] = "Mr Brown"
        res["phone_number"] = "0123.456.789"
        res["email"] = "abc@example.com"
        return res

    @api.depends('information_line_ids')
    def _type(self):
        if len(self.information_line_ids) < 5:
            self.type = False
        else:
            self.type = True
            
    def add(self):
        self.curator = self.env.user.name
    def remove(self):
        self.curator = ''

    # @api.multi 
    # def print_report(self):
    #     return self.env.ref('customer.report_customer').report_action(self)

    # @api.multi
    # def show(self):
    #     return {
    #         'name': _('test'),
    #         'view_type': 'tree',
    #         'view_mode': 'tree',
    #         'view_id': self.env.ref('customer.care.information.lines_tree').id,
    #         'res_model': 'customer.care.information.lines',
    #         'context': "{'type':'out_customer'}",
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #     }

class CustomerCareInformation(models.Model):
    _name = 'customer.care.information.lines'
    _description = "Customer care information"
    content = fields.Char('Content')
    date = fields.Date('Date')
    customer_id = fields.Many2one('customer.care',string="customer")


