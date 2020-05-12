from odoo import fields, models, api, _

class Library_Book(models.Model):
    _name = 'library.book'
    _description = 'Library Managment'
    _rec_name = 'name'

    name = fields.Char(required=True)
    category = fields.Selection([
        ('historic','Historic'),
        ('science','Science'),
        ('art','Art'),
        ('review','Review'),
        ('religion','Religion')
    ],required=True)
    book_id = fields.Char(readonly=True)
    state = fields.Selection([
        ('available','Available'),
        ('borrowed','Borrowed')
    ])
    book_state = fields.Selection([
        ('available','Available'),
        ('borrowed','Borrowed')
    ], compute='check_state',readonly=True)
    auther = fields.Many2one('library.auther', required=True)
    taxes = fields.Integer()
    quanatity = fields.Integer(required=True)
    page_num  = fields.Integer(required=True)
    book_pic  = fields.Binary(attachment=True)
    student_rel = fields.Many2one('library.student')
    
    #Sequence patient Function    
    @api.model
    def create(self, vals):
        if vals.get('book_id', _('New')) == _('New'):
            vals['book_id'] = self.env['ir.sequence'].next_by_code('book.sequence') or _('New')
        result = super(Library_Book, self).create(vals)
        return result

    # Check State Function
    def check_state(self):
        if self.quanatity == 0 :
            self.book_state = 'borrowed'
        else :
            self.book_state = 'available'    

