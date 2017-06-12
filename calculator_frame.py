#-*-coding:utf-8-*-
#Õº–ŒΩÁ√Ê
import tkinter as tk
class NUM:
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.grid(column=0,columnspan=3,sticky="E")
        
        self.zero=tk.Button(frame,text="0",fg="black")
        self.one=tk.Button(frame,text="1",fg="black")
        self.two=tk.Button(frame,text="2",fg="black")
        self.three=tk.Button(frame,text="3",fg="black")
        self.four=tk.Button(frame,text="4",fg="black")
        self.five=tk.Button(frame,text="5",fg="black")
        self.six=tk.Button(frame,text="6",fg="black")
        self.seven=tk.Button(frame,text="7",fg="black")
        self.eight=tk.Button(frame,text="8",fg="black")
        self.nine=tk.Button(frame,text="9",fg="black")
        self.eq=tk.Button(frame,text="=",fg="black")
        self.ans=tk.Button(frame,text="A",fg="black")
        
        self.one.grid(sticky="W")
        self.two.grid(row=0,column=1)
        self.three.grid(row=0,column=2,sticky="E")
        self.four.grid(row=1,column=0,sticky="W")
        self.five.grid(row=1,column=1)
        self.six.grid(row=1,column=2,sticky="E")
        self.seven.grid(row=2,column=0,sticky="W")
        self.eight.grid(row=2,column=1)
        self.nine.grid(row=2,column=2)
        self.zero.grid(row=3,column=1)
        self.eq.grid(row=3,column=2,sticky="E")
        self.ans.grid(row=3,column=0,sticky="W")
        
        
    
class TIT:
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.grid(row=0,column=0,columnspan=4)
        
        self.de_title=tk.Label(frame,text="Calculator",fg="white",bg="blue")
        self.name=tk.Label(frame,text="LT",fg="black")
        self.ent=tk.Entry(frame,text="",bg="white")
        self.de_title.grid(columnspan=4,sticky="N")
        self.name.grid(row=1,sticky="W")
        self.ent.grid(row=1,column=2,columnspan=2)
        
class CAL:
    def __init__(self,master):
        frame=tk.Frame(root)
        frame.grid(row=1,column=0,columnspan=1,sticky="W")
        
        self.plus=tk.Button(frame,text="+",fg="black")
        self.go=tk.Button(frame,text="-",fg="black")
        self.multi=tk.Button(frame,text="*",fg="black")
        self.div=tk.Button(frame,text="/",fg="black")
        
        self.plus.grid()
        self.go.grid(row=1)
        self.multi.grid(row=2)
        self.div.grid(row=3)
        

root=tk.Tk()
root.title("CALCULATOR")
tit=TIT(root)
num=NUM(root)
cal=CAL(root)
root.mainloop()
