from odoo import fields, api, models, _
from datetime import datetime

class Restored_Books(models.Model):
    _name = 'library.restored.books'
    _description = 'Restored Books'
    _rec_name = 'name'

    
    name = fields.Many2one('library.book')
    book_id = fields.Char(readonly=True, related='name.book_id')
    category = fields.Selection([
        ('historic','Historic'),
        ('science','Science'),
        ('art','Art'),
        ('review','Review'),
        ('religion','Religion')
    ],related='name.category', readonly=True)
    restored_date = fields.Datetime(default=datetime.today())
    book_pic = fields.Binary(readonly=True,related='name.book_pic')
    student = fields.Many2one('library.student')

    
