a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b and a > c:
    print("The number",a,"is greater")
elif b>a and b>c:
    print("The number",b,"is greater")
else: print("The number",c,"is greater")

