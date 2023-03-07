# Copyright (c) 2023, Abdalkarim R. Shehab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff, today, get_first_day, get_last_day


class EmployeeExcuseApplication(Document):
    def validate(self):
        self.get_hours()
        self.check_hours_allowed()
        self.date_order()


    def get_hours(self):
        total_hours = time_diff(self.to_time, self.from_time)
        self.hours = total_hours.total_seconds()/3600

    def check_hours_allowed(self):
        hours_allowed = frappe.db.get_value("Department", {"name": self.department}, "excuse_hours_alowed")
        first_month = get_first_day(today())
        last_month = get_last_day(today())
        applications_in_this_month = frappe.db.get_all("Employee Excuse Application",
                                                       {"excuse_date": ["BETWEEN",
                                                                        [first_month, last_month]],
                                                        "employee": self.employee}, "hours")
        cur_th = 0
        for cth in applications_in_this_month:
            cur_th += cth["hours"]
        check_hours = self.hours + cur_th
        if check_hours >= hours_allowed:
            frappe.throw("Sorry, You Can't Make More Applications For This Month")

    def date_order(self):
        if self.from_time > self.to_time:
            frappe.throw("Error, From Time Must Be Before To Time")
