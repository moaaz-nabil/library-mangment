from odoo import fields, models, api, _
from datetime import datetime

class Borroewd_Books(models.Model):
    _name = 'library.borrowed.books'
    _description = 'Borroewd Books'
    _rec_name = 'name'

    name = fields.Many2one('library.book', required=True)
    book_id = fields.Char(related='name.book_id', readonly=True)
    category = fields.Selection([
        ('historic','Historic'),
        ('science','Science'),
        ('art','Art'),
        ('review','Review'),
        ('religion','Religion')
    ],related='name.category', readonly=True)
    auther = fields.Char(related='name.auther.name', readonly=True)
    book_pic = fields.Binary(related='name.book_pic',readonly=True)
    student = fields.Many2one('library.student', required=True)
    borrowed_date = fields.Date(required=True)
    expect_restore_date = fields.Date(required=True)
    borrowed_days = fields.Integer(readonly=True, compute='days_betweens')

    @api.multi
    @api.depends('borrowed_date','expect_restore_date')
    def days_betweens(self):
        for rec in self:
            fmt = '%Y-%m-%d'
            start_date = str(rec.borrowed_date)
            end_date = str(rec.expect_restore_date)
            d1 = datetime.strptime(start_date, '%Y-%m-%d').date()
            d2 = datetime.strptime(end_date, '%Y-%m-%d').date()
            # d1 = datetime.strptime(start_date, fmt)
            # d2 = datetime.strptime(end_date, fmt)
            if d2 >d1 :
                rec.borrowed_days = (d2 - d1).days
            else :
                raise ValueError('end date should be superior than start day')