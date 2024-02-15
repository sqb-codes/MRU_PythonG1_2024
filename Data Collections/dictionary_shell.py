Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = (101, "Ram", 45, 67.88)
>>> data = {"id":101, "name":"Ram", "age":45, "marks":67.88}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["id"]
101
>>> data["name"]
'Ram'
>>> data["phone"] = 9898765456
>>> data
{'id': 101, 'name': 'Ram', 'age': 45, 'marks': 67.88, 'phone': 9898765456}
data.keys()
dict_keys(['id', 'name', 'age', 'marks', 'phone'])
data.values()
dict_values([101, 'Ram', 45, 67.88, 9898765456])
data.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 45), ('marks', 67.88), ('phone', 9898765456)])
data.get('name')
'Ram'
data['name']
'Ram'
data['address']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data['address']
KeyError: 'address'
data.get('address')
data.get('address', "Data is not available")
'Data is not available'
data.get('name', "Data is not available")
'Ram'
data.popitem()
('phone', 9898765456)
data.pop("name")
'Ram'
data
{'id': 101, 'age': 45, 'marks': 67.88}
data.update({"name":"Ram", "phone":9998887678})
data
{'id': 101, 'age': 45, 'marks': 67.88, 'name': 'Ram', 'phone': 9998887678}
data
{'id': 101, 'age': 45, 'marks': 67.88, 'name': 'Ram', 'phone': 9998887678}
for key in data:
    print(key)

    
id
age
marks
name
phone
for key in data:
    print(key, data[key])

    
id 101
age 45
marks 67.88
name Ram
phone 9998887678

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/dictionary_exercise.py
Salary of Akash is : 35000
data
{'names': ['Ram', 'Aman', 'Naman', 'Akash', 'Pooja'], 'dept': ['IT', 'HR', 'IT', 'HR', 'IT'], 'salary': [67000, 55000, 78000, 35000, 25000]}
data["names"]
['Ram', 'Aman', 'Naman', 'Akash', 'Pooja']
data["names"].index("Akash")
3
index = data["names"].index("Akash")
data["salary"][index]
35000

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/dictionary_exercise.py
Salary of Akash is : 35000
Total salary of IT is : 170000

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/emp_management_system.py

Login as:
1. Admin
2. Employee

Enter your choice : 1
Admin Panel

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/emp_management_system.py

Login as:
1. Admin
2. Employee

Enter your choice : 1
Admin Panel

Menu:
1. Add new employee
2. Delete an employee
3. Update an employee
4. Print all employees data
5. Search employee


= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/emp_management_system.py

Login as:
1. Admin
2. Employee

Enter your choice : 1
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 4
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 
Traceback (most recent call last):
  File "D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/emp_management_system.py", line 27, in <module>
    admin_ch = int(input("Enter your choice : "))
KeyboardInterrupt

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/emp_management_system.py

Login as:
1. Admin
2. Employee

Enter your choice : 1
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 4
All Employees Data
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 1
Enter new employee details...
Enter employee ID : 1001
Enter employee name : Ram Sharma
Enter employee department : IT
Enter employee salary : 45000
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 4
All Employees Data
Emp_ID : 1001
Emp_Name : Ram Sharma
Emp_Department : IT
Emp_Salary : 45000
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 1
Enter new employee details...
Enter employee ID : 1002
Enter employee name : Raman
Enter employee department : HR
Enter employee salary : 40000
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 4
All Employees Data
Emp_ID : 1001
Emp_Name : Ram Sharma
Emp_Department : IT
Emp_Salary : 45000
Emp_ID : 1002
Emp_Name : Raman
Emp_Department : HR
Emp_Salary : 40000
Admin Panel

    Menu:
    1. Add new employee
    2. Delete an employee
    3. Update an employee
    4. Print all employees data
    5. Search employee
    6. Logout
    
Enter your choice : 6
