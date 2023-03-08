import frappe

def execute():
    frappe.db.sql(""" update `tabWebsite Settings` set home_page = 'index' """)
