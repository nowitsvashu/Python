try:
    file=open("this.txt",'r')

except IOError as e:
    print("IOError")

except EOFError as e:
    print("EOFError")

finally:
    print("done")