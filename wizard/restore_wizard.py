from odoo import models, fields, api, _

class Restore(models.TransientModel):
    _name = 'library.restore'
    _description= 'Restore Book'

    book_name = fields.Many2one('library.borrowed.books', readonly=False)
    book_id = fields.Char(related='book_name.book_id')
    student = fields.Many2one('library.student', related= 'book_name.student')
    book_rel = fields.Many2one('library.book')

    # Restore Book Function
    def restore_book(self):
        plus_quantity = self.env['library.book'].search([('name', '=', self.book_name.name.name)])
        vals = {
            'name' : self.book_name.name.id,
            'student' : self.student.id
            }
        for rec in plus_quantity :
            rec.quanatity = rec.quanatity +1
            self.env['library.restored.books'].create(vals)
            self.env['library.borrowed.books'].search([('name', '=', self.book_name.name.id),
                                                    ('student', '=', self.student.id)]).unlink()
              

    
          