def func(x):

     if x%2 ==0:
         return True

if __name__ =='__main__':     
    a=[1,2,3,4, 10,8,20, 22, 23, 25,25,30]
    lst= list(filter(func, a))
    print(lst)
