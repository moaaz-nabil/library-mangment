from odoo import fields, api, models, _
from odoo import exceptions
from datetime import datetime

class Borrow(models.TransientModel):
    _name = 'library.borrow'
    _description = 'Borrow Book'
    book = fields.Many2one('library.book')
    student = fields.Many2one('library.student')
    borrowed_date = fields.Datetime(default=datetime.today())



    # Create Borrowed Book Record Function
    def borrow_book(self):
        for record in self :
            book_borrow_search = self.env['library.borrowed.books'].search([('name', '=', record.book.name)])
            if book_borrow_search :
                minus_quantity = self.env['library.book'].search([('name', '=', self.book.name)])
                for rec in minus_quantity :
                    if rec.quanatity >= 1 :
                        rec.quanatity = rec.quanatity -1
                        vals = {
                        'name' : self.book.id,
                        'student' : self.student.id
                           }
                        self.env['library.borrowed.books'].create(vals)
                    else :
                        raise exceptions.ValidationError(('This Is No Enough Quantity Of This Book Now'))      
            else :
                minus_quantity = self.env['library.book'].search([('name', '=', self.book.name)])
                for rec in minus_quantity :
                    if rec.quanatity >= 1 :
                        rec.quanatity = rec.quanatity -1
                        vals = {
                        'name' : self.book.id,
                        'student' : self.student.id
                        }
                        self.env['library.borrowed.books'].create(vals)
                    else :
                        raise exceptions.ValidationError('This Is No Enough Quantity Of This Book Now')      



