# Copyright (c) 2024, ebrahimelzook@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Departments(Document):

	def on_update (self):
		self.update_company_count(self.company)


	def after_delete(self):
			self.update_company_count(self.company)



	def update_company_count(self, company):
			try:
				department_count = frappe.db.count("Departments", filters={"company": company})
				frappe.db.set_value("Companys", company, "number_of_departments", int(department_count))
				frappe.db.commit()
			except:
				frappe.throw("can't calculate number of departments for company")