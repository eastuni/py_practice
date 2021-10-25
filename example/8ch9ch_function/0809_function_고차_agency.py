def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def agency(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

base = [1, 2, 3, 4, 5]
a= agency(square, base)
print(a)
print( agency(cube, base))
print( agency(quad, base))

print( agency(quad, [3,6,7,8,11,20]))
