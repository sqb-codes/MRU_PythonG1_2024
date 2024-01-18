import math
num = 100000007
sqrt = int(math.sqrt(num))
count = 0
for i in range(2, sqrt):
    count += 1
    if num % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("Total Iterations :",count)
