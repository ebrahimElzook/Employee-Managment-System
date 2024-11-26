import frappe
@frappe.whitelist()
def get_company(company=None):
    try:
        if company:
            result = frappe.get_doc("Companys",company)
        else:
         result = frappe.get_list("Companys")
        return result
    except:
        return "can't get company"