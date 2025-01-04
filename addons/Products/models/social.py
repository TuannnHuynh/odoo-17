from odoo import fields, models


class ResCompany_2(models.Model):
    _inherit = "res.company"

    user_premium = fields.Boolean(
        string="Premium User",
        help="Just for Premium user."
    )