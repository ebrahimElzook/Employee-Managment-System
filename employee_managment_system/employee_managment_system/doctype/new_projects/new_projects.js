// Copyright (c) 2024, ebrahimelzook@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('New Projects', {
	onload: function(frm) {
		frm.set_df_property('department', 'read_only', 1);
		frm.set_df_property('assigned_employees', 'read_only', 1);
		if(frm.doc.company){
			frm.set_df_property('department', 'read_only', 0);
        frm.set_query('department', function() {
            return {
                filters: {
                    'company': frm.doc.company 
                }
            };
        });
		}
		if(frm.doc.department){
			frm.set_df_property('assigned_employees', 'read_only', 0);
			frm.set_query('assigned_employees', function() {
				return {
					filters: {
						'employee_status':"Hired",
						'department':frm.doc.department
					}
				};
			});
		}
    },
	department: function(frm) {
		frm.set_df_property('assigned_employees', 'read_only', 1);
		frm.doc.assigned_employees = null
		if(frm.doc.department){
			frm.set_df_property('assigned_employees', 'read_only', 0);
			frm.set_query('assigned_employees', function() {
				return {
					filters: {
						'employee_status':"Hired",
						'department':frm.doc.department
					}
				};
			});
		}	
	},
	company: function(frm) {
		frm.set_df_property('department', 'read_only', 1);
		frm.doc.department = null
		if(frm.doc.company){
			frm.set_df_property('department', 'read_only', 0);
        frm.set_query('department', function() {
            return {
                filters: {
                    'company': frm.doc.company 
                }
            };
        });
		}
    },
});
