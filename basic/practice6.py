f = open('basedata.txt','r')
a=f.read()
f.close()

print(a)
print("====")

b = a.split('\n')

print(b)
print(b[0])

for i in range(len(b)):
    b[i] = b[i].split(',')

print(b)

# sum, average
for k in range(len(b)):
    sum = 0
    for j in range(1,4):
        b[k][j] = int(b[k][j])
        sum += b[k][j]
    b[k].append(sum)
    av = int(sum/3)
    b[k].append(av)
    print(b[k])

# sort
b.sort(key= lambda a: a[4], reverse= True)
print(b)

# ranking
for k in range(len(b)):
    b[k].append(1)

for k in range(len(b)):
    for k2 in range(k+1,len(b)):
        if b[k][4] < b[k2][4]:
            b[k][6] += 1
        elif b[k][4] > b[k2][4]:
            b[k2][6] += 1
f = open('result.txt','w')
for k in range(len(b)):
    data=','.join(map(str, b[k]))+"\n"
    f.write(data)
f.close
print('end')