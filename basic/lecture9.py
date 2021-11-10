#tuple 
my_tup=('korea','america','japan','china')

print(my_tup[2:3])
print(my_tup[2])
print(my_tup[0:2])
print("======")

#dictionary
my_dict={'kr':60, 'jp':40, 'ch':50}
print(my_dict['kr'])
my_dict['ch'] = 34
#key 로 tuple 사용 가능.
#items(),keys(),values()
for k,v in my_dict.items():
    print(k,v)
print("======")
for v in my_dict.values():
    print(v, end=' ')
print("\n======")
for k in my_dict.keys():
    print(k, my_dict[k])

print("\n======")
if not 'bt' in my_dict:
    print("no bt")

print("\n======")
#pop(), copy(), clear(), update()
j = my_dict.pop("jp")
print(j)
 
print("\n======")
b = my_dict.copy()
b['tw']=30
print(b)
print("\n======")
my_dict.clear()
print(my_dict)
print("\n======")
my_dict["am"]=20
b.update(my_dict)
print(b)

print("\n======")
a = b.get('ca','no')
print(a)

print("\n======")
a = b.get('tw','no')
print(a)

print("\n======")
a = b.setdefault('kr', 99)
print(a)

print("\n======")
a = b.setdefault('ug',66)
print(a)


# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
  
# union
print("Union :", A | B)
  
# intersection
print("Intersection :", A & B)
  
# difference
print("Difference :", A - B)
  
# symmetric difference
print("Symmetric difference :", A ^ B)