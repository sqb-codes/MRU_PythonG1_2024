import math
num = 100000007
sqrt = int(math.sqrt(num))

if num % 2 == 0 or num % 3 == 0:
    print("Number is not prime")
    exit()

count = 0
for i in range(5, sqrt, 6):
    count += 1
    if num % i == 0 or num % (i + 2) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("Total Iterations :",count)
