from tkinter import *

def    change_state():
       global   sw      
       
       if sw:
             lbl['state']= 'active'
       else:
             lbl['state']= 'disabled'
       sw= not sw
def form_set():
    global lbl
    win=Tk()
    lbl=Label(win,
              text="안녕 파이썬",
              font="HY헤드라인M 20",
              state='active',
              activeforeground="red",
              disabledforeground='blue')
    lbl.pack()

    btn=Button(win, text="눌러주세요", command= change_state)
    btn.pack()
    return win

if __name__ == '__main__':
    sw=False
    mas=form_set()
    mas.mainloop()
