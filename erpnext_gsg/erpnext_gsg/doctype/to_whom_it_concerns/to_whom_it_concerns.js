// Copyright (c) 2023, Abdalkarim R. Shehab and contributors
// For license information, please see license.txt

frappe.ui.form.on('To Whom It Concerns', {
	 employee: function(frm) {
	    if (frm.doc.employee){
	        frappe.call({
                method:"erpnext_gsg.erpnext_gsg.doctype.to_whom_it_concerns.to_whom_it_concerns.get_salary_slip",
                args:{ employee: frm.doc.employee_name},
                callback: function(r){
                    frm.set_df_property('salary', 'options', r.message);
                }
            })
	    }
	 }
});
