#lambda함수(익명함수)
k = lambda x, y : x * y
print(k(5,10))

p = lambda x, y : (x+y, x-y, x*y)
print(p(6,4))

mul = lambda x,y,z : x*y*z
print(mul(5,7,9))

print((lambda x,y,z: x*y*z)(5,7,9))

m = ["python",lambda x:x*x,100]
print(m[0])
print(m[1])
print(m[1](5))
print(m[1](m[2]))
print("==============")

#재귀호출함수
#주의 무한루프
#응용 팩토리얼, 피보나치 등

def fact(x):
    if x > 1:
        return x * fact(x-1)
    else:
        return x

print(fact(5))
print("==============")

def fibo(n):
    if n <= 2:
        return 1
    else: 
        return fibo(n-2) + fibo(n-1)

def fibo_tail(n,pre=1,prepre = 0):
    if n == 0:
        return prepre
    
    if n == 1:
        return pre

    curr = pre + prepre
    prepre = pre
    pre = curr

    return fibo_tail(n-1,pre,prepre)

import datetime
print(datetime.datetime.now().time())
# 꼬리재귀
print(fibo_tail(100))
print(datetime.datetime.now().time())
# 일반재귀
print(fibo(33))
print(datetime.datetime.now().time())

f=[]
for i in range(1,6):
    print(i)
    f.append(fibo(i))

print(f)

# 고차함수
# 인자로 다른 함수를 전달받거나 함수를 반환하는 함수
# filter(함수,리스트) 내장함수
print("==============")
def func(x):
    if x % 2 == 0:
        return True

if __name__ == '__main__':
    a = [1,2,3,4,10,8,20,22,23,25,25,30]
    lst = list(filter(func,a))
    print(lst)
    print(list(filter(lambda a: a%2 == 0,a)))

# map(함수,시쿼스) 내장함수
    print(list(map(lambda x: x * x , a)))