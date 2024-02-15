data = [
    [101, "Ram", [56,67,88,54,90]],
    [102, "Aman", [50,77,81,64,91]],
    [103, "Pooja", [88,45,78,50,77]],
    [104, "Akash", [91,84,55,44,92]]
    ]

'''
1. Find out total marks of each student
2. Calculate average marks of each student
'''
for i in range(len(data)):
    marks = data[i][2]
    name = data[i][1]
    total = 0
    for j in range(len(marks)):
        total += marks[j]

    avg = total/len(marks)
    print(f"Total Marks of {name} are : {total}")
    print(f"Average Marks of {name} are : {avg}")
    print("************")
    
     
