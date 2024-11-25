from . import __version__ as app_version

app_name = "employee_managment_system"
app_title = "Employee Managment System"
app_publisher = "ebrahimelzook@gmail.com"
app_description = "Employee Managment System BrainWise task"
app_email = "ebrahimelzook@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/employee_managment_system/css/employee_managment_system.css"
# app_include_js = "/assets/employee_managment_system/js/employee_managment_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/employee_managment_system/css/employee_managment_system.css"
# web_include_js = "/assets/employee_managment_system/js/employee_managment_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "employee_managment_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "employee_managment_system.utils.jinja_methods",
#	"filters": "employee_managment_system.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "employee_managment_system.install.before_install"
# after_install = "employee_managment_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "employee_managment_system.uninstall.before_uninstall"
# after_uninstall = "employee_managment_system.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "employee_managment_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#		"employee_managment_system.tasks.all"
#	],
	"daily": [
		"employee_managment_system.scheduled_tasks.employee.calculate_days"
	]
#	"hourly": [
#		"employee_managment_system.tasks.hourly"
#	],
#	"weekly": [
#		"employee_managment_system.tasks.weekly"
#	],
#	"monthly": [
#		"employee_managment_system.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "employee_managment_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "employee_managment_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "employee_managment_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["employee_managment_system.utils.before_request"]
# after_request = ["employee_managment_system.utils.after_request"]

# Job Events
# ----------
# before_job = ["employee_managment_system.utils.before_job"]
# after_job = ["employee_managment_system.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"employee_managment_system.auth.validate"
# ]
