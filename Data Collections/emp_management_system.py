#CRUD (Create Read Update Delete) Operations
# Emp Management System

employees = [
    {"emp_id" : 1001, "emp_name" : "Ram", "emp_dept" : "IT", "salary" : 45000},
    {"emp_id" : 1002, "emp_name" : "Akash", "emp_dept" : "IT", "salary" : 25000},
    {"emp_id" : 1003, "emp_name" : "Mohit", "emp_dept" : "HR", "salary" : 50000},
    {"emp_id" : 1004, "emp_name" : "Vaibhav", "emp_dept" : "IT", "salary" : 55000},
    ]

print("""
Login as:
1. Admin
2. Employee
""")
ch = int(input("Enter your choice : "))
if ch == 1:

    login_status = True

    while login_status:
        print("Admin Panel")
        print("""
    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    """)
        admin_ch = int(input("Enter your choice : "))
        if admin_ch == 1:
            print("Enter new employee details...")
            emp_id = int(input("Enter employee ID : "))
            emp_name = input("Enter employee name : ")
            emp_dept = input("Enter employee department : ")
            salary = input("Enter employee salary : ")
            emp = {"emp_id":emp_id, "emp_name":emp_name, "emp_dept":emp_dept,"salary":salary}
            employees.append(emp)
        elif admin_ch == 2:
            emp_id = int(input("Enter Employee ID you want to delete : "))

        elif admin_ch == 3:
            emp_id = int(input("Enter Employee ID you want to update : "))
        
        elif admin_ch == 4:
            print("All Employees Data")
            for i in range(len(employees)):
                print("Emp_ID :",employees[i]["emp_id"])
                print("Emp_Name :",employees[i]["emp_name"])
                print("Emp_Department :",employees[i]["emp_dept"])
                print("Emp_Salary :",employees[i]["salary"])
                print("*" * 50)
        elif admin_ch == 6:
            login_status = False
else:
    print("Emp Dashboard")
    emp_id = int(input("Enter Emp ID : "))
    for i in range(len(employees)):
        if employees[i]["emp_id"] == emp_id:
            print("Login Success...")
            print("Emp_ID :",employees[i]["emp_id"])
            print("Emp_Name :",employees[i]["emp_name"])
            print("Emp_Department :",employees[i]["emp_dept"])
            print("Emp_Salary :",employees[i]["salary"])
            break
    else:
        print("Login Failed...")

    
        
