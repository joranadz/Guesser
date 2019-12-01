print("CALCULATOR")
a = input("please enter first number: ")
b = input("please enter second number: ")
d = input("please enter sing: ")

if d == "+":
    c = int(a)+int(b)
elif d == "-":
    c = int(a) - int(b)
elif d == "*":
    c = int(a) * int(b)
elif d == "/":
    c = int(a) / int(b)
else:
    print("please enter correct sing")
print(c)
