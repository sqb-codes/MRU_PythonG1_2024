Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = []
data = list()
data = [101, "Akash", 78.66]
data[0]
101
data = []
data.append(12)
data
[12]
data.append(5)
data
[12, 5]
data.append(7)
data
[12, 5, 7]
data.append(17)
data
[12, 5, 7, 17]
data.append(5,6,8,4,6,8)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.append(5,6,8,4,6,8)
TypeError: list.append() takes exactly one argument (6 given)
data.append([6,5,4,5,7,12,67])
data
[12, 5, 7, 17, [6, 5, 4, 5, 7, 12, 67]]
data.pop()
[6, 5, 4, 5, 7, 12, 67]
data.extend([6,5,4,5,7,12,67])
data
[12, 5, 7, 17, 6, 5, 4, 5, 7, 12, 67]
data.pop()
67
data.pop(5)
5
data.remove(17)
data
[12, 5, 7, 6, 4, 5, 7, 12]
data.insert(3,15)
data
[12, 5, 7, 15, 6, 4, 5, 7, 12]
data.reverse()
data
[12, 7, 5, 4, 6, 15, 7, 5, 12]
sorted(data)
[4, 5, 5, 6, 7, 7, 12, 12, 15]
sorted(data, reverse=True)
[15, 12, 12, 7, 7, 6, 5, 5, 4]
data
[12, 7, 5, 4, 6, 15, 7, 5, 12]
data.sort()
data
[4, 5, 5, 6, 7, 7, 12, 12, 15]
data.sort(reverse=True)
data
[15, 12, 12, 7, 7, 6, 5, 5, 4]
for i in range(len(data)):
    print(data[i])

    
15
12
12
7
7
6
5
5
4
for i in data:
    print(i)

    
15
12
12
7
7
6
5
5
4
data = []
for i in range(50):
    if i % 2 == 0:
        data.append(i)

        
data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
data = [i for i in range(10)]
data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [i for i in range(10) if i % 2 == 0]
data
[0, 2, 4, 6, 8]
data = [[101, "Ram"],[102, "Shyam"],[103, "Aman"],[104, "Sumit"]]
data[0]
[101, 'Ram']
data[0][0]
101
data[0][1]
'Ram'
for i in range(len(data)):
    print(data[i][0], data[i][1])

    
101 Ram
102 Shyam
103 Aman
104 Sumit
data = 10
data = 10,
data
(10,)
data = 10,12,45,5,6
data
(10, 12, 45, 5, 6)
data[0] = 34
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    data[0] = 34
TypeError: 'tuple' object does not support item assignment

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/list_exercise_1.py
Total Marks of Ram are : 56
Total Marks of Ram are : 123
Total Marks of Ram are : 211
Total Marks of Ram are : 265
Total Marks of Ram are : 355
Total Marks of Aman are : 50
Total Marks of Aman are : 127
Total Marks of Aman are : 208
Total Marks of Aman are : 272
Total Marks of Aman are : 363
Total Marks of Pooja are : 88
Total Marks of Pooja are : 133
Total Marks of Pooja are : 211
Total Marks of Pooja are : 261
Total Marks of Pooja are : 338
Total Marks of Akash are : 91
Total Marks of Akash are : 175
Total Marks of Akash are : 230
Total Marks of Akash are : 274
Total Marks of Akash are : 366

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/list_exercise_1.py
Total Marks of Ram are : 355
Total Marks of Aman are : 363
Total Marks of Pooja are : 338
Total Marks of Akash are : 366

= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/list_exercise_1.py
Total Marks of Ram are : 355
Average Marks of Ram are : 71.0
Total Marks of Aman are : 363
Average Marks of Aman are : 72.6
Total Marks of Pooja are : 338
Average Marks of Pooja are : 67.6
Total Marks of Akash are : 366
Average Marks of Akash are : 73.2
>>> 
= RESTART: D:/Xebia/2024/ManavRachna Python/Codes Group 1/Data Collections/list_exercise_1.py
Total Marks of Ram are : 355
Average Marks of Ram are : 71.0
************
Total Marks of Aman are : 363
Average Marks of Aman are : 72.6
************
Total Marks of Pooja are : 338
Average Marks of Pooja are : 67.6
************
Total Marks of Akash are : 366
Average Marks of Akash are : 73.2
************
data = (101, "Ram", 30)
id, name, age = data
id
101
name
'Ram'
age
30
id, name = data
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    id, name = data
ValueError: too many values to unpack (expected 2)
