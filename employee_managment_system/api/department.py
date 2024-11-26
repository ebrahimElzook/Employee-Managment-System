import frappe
@frappe.whitelist()
def get_department(department=None):
    try:
        if department:
            result = frappe.get_doc("Departments",department)
        else:
         result = frappe.get_list("Department")
        return result
    except:
        return "can't get department"