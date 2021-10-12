import sys
while True:
    a = input("1st num: ")
    b = input("2nd num: ")

    try:
        a = int(a)
        b = int(b)
        c = a/b
    except:
        e = str(sys.exc_info()[1])
        if "division by zero" in e:
            print("===== It cannot be divided by zero.")
        elif "invalid literal for int()" in e:
            print("===== Please enter only numbers.")
    else:
        print("The result of division is ",c)