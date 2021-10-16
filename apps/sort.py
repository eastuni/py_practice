iss_cnt='''Backup 9
Bxm 6
CBP 29
CCT 3
Docs 7
Etc 3
PF 18
POC 8
Portal 43
System 57
계정 13
담벼락 6'''

b = iss_cnt.split('\n')
print(b[0])

for i in range(len(b)):
    b[i] = b[i].split(' ')
    b[i][1] = int(b[i][1])

print(b[0])

print("=========")

b.sort(key= lambda a: a[1], reverse= True)
for i in range(len(b)):
    print(i+1 , b[i])