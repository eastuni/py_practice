my_list = ['korea', 'america', 'china', 'japan']

print(my_list)
print(my_list[0])
print(my_list[3])
print(my_list[-1])
print(len(my_list))

#slice
print(my_list[0:2])

if "america" in my_list:
    print("exist america")

my_list[2] = 2500
print(my_list)

#print(my_list[5])

#list,tuple,dict,Set

a = list(range(5))
print(a)

b = a + a
print(b)

c = [a,"korea","china"]
print(c)
print(c[0][2])

a.append(0)
a.insert(2,"kim")
print(a)

print(a.count(0))

print(a.index('kim'))

a.remove('kim')

a.sort()

print(a)

a.extend([40,50,60])
print(a)

a.append([40,50,60])
print(a)