from odoo import fields, api, models, _

class Student(models.Model):
    _name= 'library.student'
    _description = 'Students'
    _rec_name = 'name'

    name = fields.Char()
    student_id = fields.Char(readonly=True)
    phone = fields.Char()
    his_borrowed_books = fields.Many2many('library.book','student_rel', compute='get_borrowed_books',readonly=True)

    #Sequence patient Function    
    @api.model
    def create(self, vals):
        if vals.get('student_id', _('New')) == _('New'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        result = super(Student, self).create(vals)
        return result


    # Get Student Borrowed Books
    def get_borrowed_books(self):
        borrowed_books = self.env['library.borrowed.books'].search([('student', '=', self.id)])
        for rec in borrowed_books :
           if rec.name.name in self.his_borrowed_books : 
            return rec.name.name
           else :
               self.his_borrowed_books = rec.name

