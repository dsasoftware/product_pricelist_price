# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from datetime import date
import pdb

class product_product(osv.osv):
    _name = 'product.product'
    _inherit = 'product.product' 

    def _fnct_pricelist_price(self, cr, uid, ids, field_name, args, context=None):
        product_pricelist_obj = self.pool.get('product.pricelist')

        if context is None:
            context = {}
	res = {}
        for product in self.browse(cr, uid, ids, context=context):
            res[product.id] = self.pool.get('product.pricelist').price_get(cr,uid,[1],product.id,1.0,1,{'uom':1,'date':date.today()})[1]
        return res

    _columns = {
        'pricelist_price': fields.function(_fnct_pricelist_price, string='Pricelist Price'),
    }

product_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
