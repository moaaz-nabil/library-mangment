from odoo import fields, api, models, _

class auther(models.Model):
    _name = 'library.auther'
    _description = 'Authers'
    _rec_name = 'name'

    name = fields.Char()
    his_books = fields.Many2many('library.book',compute='auther_book',readonly=True)
    auther_pic = fields.Binary(attachment=True)


    # His Books Function
    @api.one  
    def auther_book(self):
        auther_books = self.env['library.book'].search([('auther', '=', self.id)])
        for rec in auther_books :
            if rec in self.his_books :
                return rec
            else :
                self.his_books = rec    
