# -*- coding: utf-8 -*-
{
    'name': "library",
    'version': '12.0.1.0.0',
    'summary': """
        Library Managment App""",

    'description': """
        Library Managment App
            """,

    'author': "Moaz Nabil",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'wizard/borrow_book.xml',
        'wizard/restore_view.xml',
        'data/book_sequence.xml',
        'data/student_sequence.xml',
        'views/templates.xml',
        'views/library_book.xml',
        'views/library_auther.xml',
        'views/library_borroewed_books.xml',
        'views/library_menu.xml',
        'views/library_restored_books.xml',
        'views/library_student.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'data/library_demo_view.xml',

    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
