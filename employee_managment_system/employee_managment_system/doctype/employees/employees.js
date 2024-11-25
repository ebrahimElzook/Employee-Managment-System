// Copyright (c) 2024, ebrahimelzook@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employees', {
	onload: function(frm) {
		// show only departments following the selected company
		frm.set_df_property('department', 'read_only', 1);
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
		// Show 'hired_on' ,'number_of_assigned_projects'and  'days_employed' fields on load
		if(frm.doc.employee_status != "Hired"){
		frm.set_df_property('hired_on', 'hidden', 1);
		frm.set_df_property('days_employed', 'hidden', 1);
		frm.set_df_property('number_of_assigned_projects', 'hidden', 1);
		}
		else{
		frm.set_df_property('hired_on', 'hidden', 0);
		frm.set_df_property('days_employed', 'hidden', 0);
		frm.set_df_property('number_of_assigned_projects', 'hidden', 0);
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
