#내장함수
#모듈함수
#객체의 함수(메소드)
#사용자 정의 함수

def division(x,y):
    if int(y) == 0:
        res = 'unavailable'
    else:
        res = int(x)/int(y)
    return res


def end_check(x,y):
    if x.isnumeric() and y.isnumeric():
        return False
    else:
        return True

print(division(10,5))
print(end_check("10","t"))


def func(x, y):
    x = 10
    y = 20
    print("in func->",x,y,a)
# 메인 쪽 변수에 접근가능.
# 할당하는 순간 지역변수로 바뀜

def func2():
    a[0] = 100

#기본값 
def increment(data, interval = 1):
    data += interval
    return data

if __name__=='__main__':
    a = 100
    b = 200
    func(a,b)
    print("main",a,b)
# 전달한 메인 변수 값이 바뀌지 않음.
# list 내의 값은 가능.
    a = [10,20,30,40]
    print(a)
    func2()
    print(a)

    print(increment(10))
    print(increment(10,10))

def find(src,ch,all=False):
    position=[]
    for i in range(len(src)):
        if src[i] == ch:
            position.append(i)
            if not all:break
    return position

s= "배구 우리나라 우생순 우승"
print(find(s,'우'))
print(find(s,'우',True))

def printing(src, repetition = 1):
    for i in range(repetition):
        print(src)

printing("korea")
print("====")
printing(repetition = 5, src="korea")

from tkinter import *

def change_state():
    global sw
    if sw:
        lbl['state'] = 'active'
    else:
        lbl['state'] = 'disabled'
    sw = not sw

def form_set():
    global lbl
    win=Tk()
    lbl=Label(win
            ,text="hello, python"
            ,font="HY헤드라인M 20"
            ,state='active'
            ,activeforeground="red"
            ,disabledforeground='blue')
    lbl.pack()
    btn=Button(win, text="click", command = change_state)
    btn.pack()
    return win

if __name__=='__main__':
    sw = False
    mas=form_set()
    mas.mainloop()
