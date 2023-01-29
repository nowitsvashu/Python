def function(*args):
    print(type(args))
    if len(args) == 3:
        print("The name is ", args[0] ,"and the age is ",args[1],"and the roll no. is ",args[2])

    else: print("The name is ", args[0] ,"and the age is ",args[1])

function("Vashu",21)

function("Vashu",22,4842)