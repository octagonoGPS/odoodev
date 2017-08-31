# Develop Application
from openerp import models, fields

class Develop_sale_order_template(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'	

    calories = fields.Integer("Calories")