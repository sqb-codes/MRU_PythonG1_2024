num = 17
count = 0
for i in range(2, num):
    count += 1
    if num % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("Total Iterations :",count)
