## ERPNext GSG
This App Includes:

1- In Journal Entry in field Entry Type Options “Inter Company Journal Entry” and “Deferred Expense” are Removed.
2- In Payment Entry made Series = ‘GSG-JV-.YYYY.-’ for every New Payment Entry Created.
3- when submitting Material Request  with values Purpose “Material Issue” , Target Warehouse and Items, Created new Stock Entry with Stock Entry Type “Material Issue”,  Target Warehouse and Items , also added value name material request to field material_request in Items.
4- Added field “Sales order time” to Sales order and it is Mandatory.
5- Added filter “From Time”  and “To Time” and it's Mandatory to report Sales Order Analysis and field “Sales order time” in Sales order used to filter result.
6- Created Sales Invoice Format name sales_invoice_gsg includes QR code and specific style.
7- Added custom Fields Check In and Check Out To Attendance.
8- Created script report name “Attendance Working Hours” with filters “From Date”, “To Date”, “Employee” and “Department” with columns Attendance Date, Employee , Employee Name , Check in and Check Out, added column Working Hours after column Check Out and calculates value Working Hours in report , if attendance does not have check out or check out make Working Hours zero, added column “View Attendance“ after column  Working Hours  when user click on View Attendance will open attendance form in new tab browser.
9- Added Form Employee Excuse application and have fields Employee , Employee Name, Department , Excuse Date , From Time, To Time, Hours and Reason.
10- Added custom field “Excuse Hours ALowed” to Department form.
11- When saving Excuse application Hours are Calculated and do a validation must be less than  value “Excuse Hours ALowed”  in one Month “Current Month” and from time must be before to time.
12- Created Form “To Whom It Concerns” with fields Employee , Employee Name, Department,  Date of Joining and Salary , when user selects Employee get Employee Name, Department and  Date of Joining from employee also get Salary From Last Salary Slip For Same Employee.
13- Customized HR Workspace, added link for  Employee Excuse application ,  Attendance Working Hours  and To Whom It Concerns.
14- Created Print Format name “Employee Format GSG” having specific employee card design.
15- Added page to be the home page.



#### License

MIT
