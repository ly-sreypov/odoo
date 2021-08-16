# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, tools, _


class AccountInvoiceInherit ( models.Model ):
    _inherit = 'account.move'
    _description = 'Account Invoice Customized'


