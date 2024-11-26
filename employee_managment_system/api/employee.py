import frappe

@frappe.whitelist()
def get_employee(employee=None):
    try:
        if employee:
            result = frappe.get_doc("Employees",employee)
        else:
         result = frappe.get_list("Employees")
        return result
    except:
        return "can't get employee"

@frappe.whitelist()
def post_employee(company,department,employee_name,email_address,mobile_number=None,address=None,title=None):
   try:
     new_doc = frappe.get_doc({
    'doctype': 'Employees',
    'company': company,
    'department': department,
    'employee_name':employee_name,
    'email_address':email_address,
    'mobile_number':mobile_number,
    'address':address,
    'title':title
})
     new_doc.insert()
     new_doc.save()
     return "employee creation success"
   except:
      return "employee creation failed"


@frappe.whitelist()
def edit_employee(email_address,employee_name=None,company=None,department=None,mobile_number=None,address=None,title=None):
   try :
       employee_doc = frappe.get_doc("Employees",email_address)
       if employee_name :
          employee_doc.employee_name = employee_name
       if company :
          employee_doc.company = company
       if department :
          employee_doc.department = department
       if mobile_number :
          employee_doc.mobile_number = mobile_number
       if address :
           employee_doc.address = address
       if title :
           employee_doc.title = title
       employee_doc.save()
       return "employee edit success"   
   except:
    return "employee edit failed"   
   
@frappe.whitelist()
def delete_employee(email_address):
   try :
       frappe.delete_doc("Employees",email_address)
       return "employee delete success"   
   except:
    return "employee delete failed"   