a={'1101':['삼 립 빵', 66,300000], '1102':['서울우유', 45,420000], '1105':['퐁    퐁', 46,400200], '1108':['민 트 껌', 90,170000], '1109':['감 자 깡', 66,320900]}

b={'1102':['서울우유', 44, 390000], '1103':['테 이 프', 30, 270000], '1105':['퐁    퐁', 80,710000], '1107':['커    피', 44,329000], '1108':['민 트 껌', 57, 102000], '1109':['감 자 깡', 50, 200200]}

c=a.copy()
for k,v in a.items():
    if k in b.keys():
        temp=a[k][0], a[k][1] + b[k][1], a[k][2] + b[k][2]
        c[k] = list(temp)
    else:
        c[k] = a[k]

for k,v in b.items():
    if k in a.keys():
        continue
    else:
        c[k] =  b[k]

for k,v in c.items():
    print("{}    {}    {:>4d}    {:>10,d}    ".format(k,v[0],v[1],v[2]))

print("=================")
c = a.copy()

for k,v in b.items():
    c.setdefault(k,["",0,0])
    temp=v[0], c[k][1] + v[1], c[k][2] + v[2]
    c[k] = list(temp)


for k,v in c.items():
    print("{}    {}    {:>4d}    {:>10,d}    ".format(k,v[0],v[1],v[2]))
