# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invoicing Customized',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
    Change the properties of Odoo Invoice
    """,
    'depends': ['account'],
    'data': [
        'views/account_invoice_customized_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
