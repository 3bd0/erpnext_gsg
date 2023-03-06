frappe.ui.form.on('Sales Invoice',{
    setup: function(frm) {
        set_field_options("naming_series",["ACC-SINV-.YYYY.-","ACC-SINV-RET-.YYYY.-","sales_invoice_gsg"])
    }
})
