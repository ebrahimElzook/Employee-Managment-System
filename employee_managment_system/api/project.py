import frappe

@frappe.whitelist()
def get_project(project=None):
    try:
        if project:
            result = frappe.get_doc("New Projects",project)
        else:
         result = frappe.get_list("New Projects")
        return result
    except:
        return "can't get project"

@frappe.whitelist()
def post_project(company,department,project_name,description=None,start_date=None,end_date=None):
   try:
     new_doc = frappe.get_doc({
    'doctype': 'New Projects',
    'company': company,
    'department': department,
    'project_name':project_name,
    'description':description,
    'start_date':start_date,
    'end_date':end_date
})
     new_doc.insert()
     new_doc.save()
     return "project creation success"
   except:
      return "project creation failed"


@frappe.whitelist()
def edit_project(project_name,company=None,department=None,description=None,start_date=None,end_date=None):
   try :
      project_doc = frappe.get_doc("New Projects",project_name)
      if description :
          project_doc.description = description
      if company :
          project_doc.company = company
      if department :
          project_doc.department = department
      if start_date :
          project_doc.start_date = start_date
      if end_date :
           project_doc.end_date = end_date
      project_doc.save()
      return "project edit success"   
   except:
    return "project edit failed"   
   
@frappe.whitelist()
def delete_employee(project_name):
   try :
       frappe.delete_doc("New Projects",project_name)
       return "project delete success"   
   except:
    return "project delete failed"   