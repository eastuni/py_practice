data="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(26):
    s = data[i:26] + data[0:i]
    print("{:2d}   {}".format(i, s))