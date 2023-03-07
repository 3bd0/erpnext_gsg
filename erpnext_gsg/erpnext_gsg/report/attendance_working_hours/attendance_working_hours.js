// Copyright (c) 2023, Abdalkarim R. Shehab and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
		{'fieldname': 'from_date',
		 'label': 'From Date',
		  'fieldtype': 'Date',
		  'default': frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		  },
		{'fieldname': 'to_date',
		 'label': 'To Date',
		 'fieldtype': 'Date',
         'default': frappe.datetime.get_today()
         },
		{'fieldname': 'employee',
		'label': 'Employee',
		'fieldtype': 'Link',
		'options': 'Employee',
		},
		{'fieldname': 'department',
		'label': 'Department',
		'fieldtype': 'Link',
		'options': 'Department',
		}
	]
};
