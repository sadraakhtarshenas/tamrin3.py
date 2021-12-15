w = float(input("pleas enter your number one:"))
a = input("What operation do you want me to do?:")
f = float(input("pleas enter your number two:"))



if a == "+":
    result = w + f
if a == "-":
    result = w - f
if a == "*":
    result = w * f
if a == "/":
    if a != 0:
        result = w / f
    else:
       result("can not divide by zero!!")
print(result)