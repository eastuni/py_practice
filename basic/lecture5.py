f = open('test.txt','r')

mydata = f.read()
print(mydata)

data = mydata.split('\n')
print(data)
f.close()
print("====")
f = open('test.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()
print("====")
f = open('test.txt','r')
for line in f:
    print(line,end='')
f.close()
print("====")


#f2 = open('test2.txt','w')
#f2.write(mydata)
#f2.close()

data ="dab","asg","asdd"
wf = open('test2.txt','w')
st = '\n'.join(data)
wf.write(st)
wf.writelines(data)
wf.close()

#r(read only),w(write only,new),a(write append),r+(read write),w+(read write new),a+(read write append)




