from tkinter import *

class MyDialog:
    def __init__(self, parent):
        Label(parent, text="값입력").pack()
        self.e = Entry(parent)
        self.e.pack(padx=5)
        self.b = Button(parent, text="확인", command=self.ok_click)
        self.b.pack(pady=5)
    def ok_click(self):
        print("value is", self.e.get())
class   BranchDialog(MyDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.b2 = Button(parent, text="취소", command=self.cancel_click)
        self.b2.pack(pady=5)
    def  cancel_click(self):
        print("취소를 눌렀습니다.")
root = Tk()
a=MyDialog(root)
b=BranchDialog(Tk())  
root.mainloop()
