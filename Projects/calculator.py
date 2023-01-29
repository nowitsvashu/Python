def add(a, b):
    sum = a+b
    return sum


def sub(a, b):
    sub = a-b
    return sub


def mul(a, b):
    mul = a*b
    return mul


def div(a, b):
    div = a/b
    return div


print("Choose an Operation:")
print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")


while True:
    choice = input("Choose (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        if choice == '1':
            print(x, "+", y,"=",add(x,y))
        elif choice == '2':
            print(x, "-", y,"=",sub(x,y))
        elif choice == '3':
            print(x, "*", y,"=",mul(x,y))
        elif choice == '4':
            print(x, "/", y,"=",div(x,y))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
else:
    print("Please emter a valid input")
