# Copyright (c) 2024, ebrahimelzook@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Employees(Document):
	def onload(self):
		if self.is_new() :
			old_company = None
			old_department = None

		else :
			old_company=self.company
			old_department=self.department
			company_count = frappe.db.count("Employees",filters={"company":old_company})
			department_count = frappe.db.count("Employees",filters={"department":old_department})
			# save to db because cant save in validate
			frappe.db.set_value('Companys', old_company, {
    'number_of_employees': company_count
})
			frappe.db.set_value('Departments', old_department, {
    'number_of_employees': department_count
})
			frappe.db.commit()
	def before_save(self):
		if  (not self.mobile_number.startswith('0'))  or len(self.mobile_number) != 11:
			frappe.throw("The mobile number is not correct")
		self.old_company =self.get_db_value("company")
		self.old_department =self.get_db_value("department")

	def on_update (self):
		if self.is_new():
			self.update_company_count(self.company)
			self.update_department_count(self.department)
		if  self.old_company:
			new_company = self.company

            # Update the number of employees for the old company
			if self.old_company:
				self.update_company_count(self.old_company)

            # Update the number of employees for the new company
			if new_company:
				self.update_company_count(new_company)

		if self.old_department:
				new_department = self.department
			 # Update the number of employees for the old department
				if self.old_department :
					self.update_department_count(self.old_department)
			 # Update the number of employees for the new department
				if new_department:
					self.update_department_count(new_department)


	def after_delete(self):
        # Update the number of employees for the company
			if self.company:
				self.update_company_count(self.company)
			if self.department:
				self.update_department_count(self.department)


	def update_company_count(self, company):
			employee_count = frappe.db.count("Employees", filters={"company": company})
			frappe.db.set_value("Companys", company, "number_of_employees", int(employee_count))
			frappe.db.commit()

	def update_department_count(self, department):
			employee_count = frappe.db.count("Employees", filters={"department": department})
			frappe.db.set_value("Departments", department, "number_of_employees", int(employee_count))
			frappe.db.commit()

		

