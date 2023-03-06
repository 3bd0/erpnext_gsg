frappe.ui.form.on('Payment Entry',{
    setup: function(frm) {
        set_field_options("naming_series",["ACC-PAY-.YYYY.-","GSG-JV-.YYYY.-"])
    }
})
