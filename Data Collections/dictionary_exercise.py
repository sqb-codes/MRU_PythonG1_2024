data = {
    "names" : ["Ram", "Aman", "Naman", "Akash", "Pooja"],
    "dept" : ["IT", "HR", "IT", "HR", "IT"],
    "salary" : [67000,55000,78000,35000,25000]
    }

'''
1. What is the salary of Akash ?
2. Average salary of IT Department ?
'''
index = data["names"].index("Akash")
salary = data["salary"][index]
print(f"Salary of Akash is : {salary}")

sal = 0
for i in range(len(data["dept"])):
    if data["dept"][i] == "IT":
       sal += data["salary"][i]

print("Total salary of IT is :",sal)


    
