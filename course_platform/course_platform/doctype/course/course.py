# Copyright (c) 2023, sudo and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Course(WebsiteGenerator):
	def get_context(self, context):
		context.publisher = frappe.db.get_value(
			"Publisher", self.publisher,['creator'], as_dict=True
		)
		context.category = frappe.db.get_value(
            "Category", self.category, ['title'], as_dict=True
        )





