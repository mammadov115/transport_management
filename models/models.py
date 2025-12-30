# # -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class TransportManagement(models.Model):
#     _name = 'transport.management'
#     _description = 'Transport Management'

#     name = fields.Char(string="Order Ref", required=True, copy=False, readonly=True, default="New")
#     carrier_info = fields.Char(string="Carrier Info", required=True)
#     delivery_period = fields.Date(string="Delivery Period")
#     from_location = fields.Char(string="From Location")
#     to_location = fields.Char(string="To Location")
#     product_id = fields.Many2one('product.product', string="Product")
#     transport_mode = fields.Selection([
#         ('air', 'Air'),
#         ('sea', 'Sea'),
#         ('land', 'Land'),
#     ], string="Transport Mode")
#     incoterm = fields.Char(string="Incoterm")


#     @api.model_create_multi
#     def create(self, vals_list):
#         for vals in vals_list:
#             if vals.get('name', 'New') == 'New':
#                 vals['name'] = self.env['ir.sequence'].next_by_code('transport.management') or 'New'
#         return super(TransportManagement, self).create(vals_list)

