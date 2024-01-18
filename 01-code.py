a = 34
b = 20
c = a + b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum of %d and %d is %d"%(a,b,c))

print("Sum of {} and {} is {}".format(a,b,c))

print("Sum of {1} and {2} is {0}".format(c,a,b))

#f-strings
print(f"Sum of {a} and {b} is {c}")
