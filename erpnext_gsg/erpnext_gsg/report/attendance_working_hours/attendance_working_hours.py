# Copyright (c) 2023, Abdalkarim R. Shehab and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    conditions = get_conditions(filters)
    data = get_data(conditions, filters)
    return columns, data


def get_conditions(filters):
    conditions = ""
    if filters:
        if filters.get("from_date"):
            conditions += "and attendance_date > %(from_date)s "
        if filters.get("to_date"):
            conditions += "and attendance_date < %(to_date)s"
        if filters.get("employee"):
            conditions += "and employee = %(employee)s"
        if filters.get("department"):
            conditions += "and department = %(department)s"
    return conditions


def get_columns():
    columns = [
        {'fieldname': 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
        {'fieldname': 'employee', 'label': 'Employee', 'fieldtype': 'Link', 'options': 'Employee'},
        {'fieldname': 'employee_name', 'label': 'Employee Name', 'fieldtype': 'Data'},
        {'fieldname': 'check_in', 'label': 'Check In', 'fieldtype': 'Time'},
        {'fieldname': 'check_out', 'label': 'Check Out', 'fieldtype': 'Time'},
        {'fieldname': 'working_hours', 'label': 'Working Hours', 'fieldtype': 'Float'},
        {'fieldname': 'view', 'label': 'View', 'fieldtype': 'HTML',
         'options': '<a target="_blank" href="#">view</a>'},
    ]
    return columns


def get_data(conditions, filters):
    data = frappe.db.sql(
        """SELECT name as view, employee, employee_name, attendance_date, check_in, check_out,
         CASE WHEN check_in and check_out THEN time(check_out-check_in) ELSE 0 END as 
        working_hours FROM `tabAttendance` WHERE docstatus = 1 {conditions}""".format(conditions=conditions), filters,
        as_dict=1)
    for x in data:
        x["view"] = f""" <a target="_blank" href="#" 
        onclick = 'window.open("http://0.0.0.0:8000/app/attendance/{x["view"]}");return false;'>view</a>"""
    return data
