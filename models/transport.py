from odoo import models, fields, api


class TransportManagement(models.Model):
    """
    Main model for managing transport orders.
    Handles logistics details, transport modes, and linked product lines.
    """
    _name = 'transport.management'
    _description = 'Transport Management'

    # --- Fields Definition ---
    name = fields.Char(
        string="Order Ref", 
        required=True, 
        copy=False, 
        readonly=True, 
        default="New"
    )
    carrier_info = fields.Char(string="Carrier Info", required=True)
    delivery_period = fields.Date(string="Delivery Period")
    from_location = fields.Char(string="From Location")
    to_location = fields.Char(string="To Location")
    
    # Selection for different logistics methods
    transport_mode = fields.Selection([
        ('air', 'Air'),
        ('sea', 'Sea'),
        ('land', 'Land'),
    ], string="Transport Mode")
    
    incoterm = fields.Char(string="Incoterm")
    
    # Relationship to detailed product lines
    line_ids = fields.One2many(
        'transport.management.line', 
        'transport_id', 
        string='Products'
    )

    # --- CRUD Methods ---
    @api.model_create_multi
    def create(self, vals_list):
        """
        Override create method to assign a unique sequence number 
        from 'ir.sequence' when a new record is created.
        """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                # Fetch sequence based on the model's code
                vals['name'] = self.env['ir.sequence'].next_by_code('transport.management') or 'New'
        
        return super(TransportManagement, self).create(vals_list)


class TransportManagementLine(models.Model):
    """
    Line item model for Transport Management.
    Stores specific products and quantities associated with a transport order.
    """
    _name = 'transport.management.line'
    _description = 'Transport Order Line'

    # Link back to the parent transport record
    transport_id = fields.Many2one(
        'transport.management', 
        string='Transport Reference', 
        ondelete='cascade'
    )
    
    product_id = fields.Many2one(
        'product.product', 
        string='Product', 
        required=True
    )
    
    quantity = fields.Float(string='Quantity', default=1.0)
    
    uom_id = fields.Many2one(
        'uom.uom', 
        string='Unit of Measure'
    )