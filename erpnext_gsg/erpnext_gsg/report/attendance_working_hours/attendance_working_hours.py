# Copyright (c) 2023, Abdalkarim R. Shehab and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import time_diff


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        {'fieldname': 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
        {'fieldname': 'employee', 'label': 'Employee', 'fieldtype': 'Link', 'options': 'Department'},
        {'fieldname': 'employee_name', 'label': 'Employee Name', 'fieldtype': 'Data'},
        {'fieldname': 'check_in', 'label': 'Check In', 'fieldtype': 'Time'},
        {'fieldname': 'check_out', 'label': 'Check Out', 'fieldtype': 'Time'},
        {'fieldname': 'working_hours', 'label': 'Working Hours', 'fieldtype': 'Float',
         'default': time_diff('check_out', 'check_in')},
    ]
    return columns


def get_data(filters):
    return frappe.db.get_all('Attendance', ['employee', 'employee_name', 'attendance_date', 'check_in', 'check_out', ],
                             filters=filters)
