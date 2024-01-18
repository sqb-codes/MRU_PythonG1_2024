a,b,c = 12,20,45

if a > b and a > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")


output = "A" if a > b and a > c else "B" if b > a and b > c else "C"
print(output,"is greatest")
