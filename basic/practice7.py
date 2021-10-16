def my_com(x,y):
    ad = x + y
    sb = x - y
    mt = x * y
    if y != 0:
        dv = x / y
    else :
        dv = "unavailable"
    return ad, sb, mt, dv

print (my_com(10,4))
print (my_com(10,0))