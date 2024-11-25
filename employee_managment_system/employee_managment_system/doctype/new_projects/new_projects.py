# Copyright (c) 2024, ebrahimelzook@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NewProjects(Document):
	def before_save(self):
		self.old_company =self.get_db_value("company")
		self.old_department =self.get_db_value("department")
		if frappe.get_list('Project Employees', filters={'parent': self.name}):
			self.old_employees=frappe.get_list('Project Employees', filters={'parent': self.name},fields={'employee'})
	def on_update (self):
		if self.is_new():
			if frappe.get_list('Project Employees', filters={'parent': self.name}):
				new_employees = frappe.get_list('Project Employees', filters={'parent': self.name},fields={'employee'})
			self.update_company_count(self.company)
			self.update_department_count(self.department)
			self.update_employees_count(new_employees)
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
				self.update_department_count(self.old_department)
			 # Update the number of employees for the new department
				if new_department:
					self.update_department_count(new_department)

		if self.old_employees:
			self.update_employees_count(self.old_employees)
			if frappe.get_list('Project Employees', filters={'parent': self.name}):
				new_employees = frappe.get_list('Project Employees', filters={'parent': self.name},fields={'employee'})
				self.update_employees_count(new_employees)

	def after_delete(self):
        # Update the number of employees for the company
			if self.company:
				self.update_company_count(self.company)
			if self.department:
				self.update_department_count(self.department)
			if frappe.get_list('Project Employees', filters={'parent': self.name}):
				employees =frappe.get_list('Project Employees', filters={'parent': self.name})
				self.update_employees_count(employees)


	def update_company_count(self, company):
			project_count = frappe.db.count("New Projects", filters={"company": company})
			frappe.db.set_value("Companys", company, "number_of_projects", int(project_count))
			frappe.db.commit()

	def update_department_count(self, department):
			project_count = frappe.db.count("New Projects", filters={"department": department})
			frappe.db.set_value("Departments", department, "number_of_projects", int(project_count))
			frappe.db.commit()	

	def update_employees_count(self, employees):
			for employee in employees:		
				project_count = frappe.db.count("Project Employees", filters={"employee": employee.employee})
				frappe.db.set_value("Employees", employee.employee, "number_of_assigned_projects", int(project_count))
				frappe.db.commit()

