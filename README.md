## Employee Managment System

Employee Managment System is a system created specifically so you can have employees , companys , projects ,and departments 
 
First : approaches :
  1-The doctypes was created through frappe pannel and had permissions set for them with required fields set as required.
  2-The validations of calculating numbers was set as server side scripts in the python file of each doctype.
  3-Having special filters for the the link fields was set as client side scripts in the js file of each doctype. 
  4-The calculation of number of days an employee was hired for was set as a background job so that employees number of days would refresh automatically.
  5-APIs was added to api folder and was programed in python .
  
Second : How to setup:
  this is a frappe app so it can be installed through being downloaded with bench command like this : bench get-app https://github.com/ebrahimElzook/Employee-Managment-System.git 
  after that being installed like this: bench --site <site name> install-app Employee-Managment-System.
  
Third : Tasks completion :
  all doctypes was created with all fields intact but with names like this :
    User Account => User Account
    Company => Companys.
    Employee => Employees.
    Department => Departments.
    Project => Projects.
  all APIs was created even bonus Apis.
  all validation was done.
  workflow for employee added.
Fourth : APIs End Points:
all APIs have headrs with key :"Authorization" value : "token user_key:user_secret"
  Employee APIs :
    get :{{base_url}}/api/method/employee_managment_system.api.employee.get_employee    the body can be empty or {"email_address":"test@example.com"}
    post new  : {{base_url}}/api/method/employee_managment_system.api.employee.post_employee the body can be like this
        {"company":"test","department":"department_test","employee_name":"ebrahim","mobile_number":"011225544778","email_address":"test@example.com","title":"ADMIN","address":"haram"} 
           with mobile_number ,address and title as options
    edit old : {{base_url}}/api/method/employee_managment_system.api.employee.edit_employee
      {"company":"test","department":"department_test","employee_name":"ebrahim","mobile_number":"011225544778","email_address":"test@example.com","title":"ADMIN","address":"haram"} 
        with only email as required
    delete employee : {{base_url}}/api/method/employee_managment_system.api.employee.delete_employee   the body would be just email {"email_address":"test@example.com"} 
  Department API:
    get : {{base_url}}/api/method/employee_managment_system.api.department.get_department   the body can be empty or {"department":"department_test"}
  Company API:
    get : {{base_url}}/api/method/employee_managment_system.api.company.get_company   the body can be empty or {"company":"test"}
  Project APIs: 
    get : {{base_url}}/api/method/employee_managment_system.api.project.get_project   the body can be empty or {"project":"test-project"}
    post new  : {{base_url}}/api/method/employee_managment_system.api.project.post_project the body can be like this
      {"company":"test","department":"department_test","project_name":"project-test","description":"this is project","start_date":"2024-11-26","end_date":"2024-11-30"} 
           with description ,start_date and end_date as options
    edit old : {{base_url}}/api/method/employee_managment_system.api.project.edit_project
     {"company":"test","department":"department_test","project_name":"project-test","description":"this is project","start_date":"2024-11-26","end_date":"2024-11-30"} 
        with only project_name as required
     delete project : {{base_url}}/api/method/employee_managment_system.api.project.delete_project   the body would be just  {"project":"test-project"}
