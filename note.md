# GUI 学习 #
----------
## tkinter模块 ##
【注意开头字母的大写】  
import tkinter

**Tk()**: tops=tkinter.Tk()【创建顶层窗口，必须先要创建它】  
**mainloop()**: tops.mainloop()【将对象进行实例化】  
**geometry**: tops.geometry("500x300+600+500")【设置大小、原始位置】  
**wm_title()**: tops.wm_title("name")【窗口名字】  
**Label()**: tkinter.label(tops,text="",bitmap=""，image=""，textvariable=varl,font=("微软雅黑"，10),fg="red",bg=""，width=10，height=3，anchor=)【创建标签，bitmap使用位图,bg背景色，anchor设置文本位置（n/s/e/w/ws…）】  
**Entry**：  
**ScrolledText()**: text=scrolledtext(tops,frot=)【设定text为滚动条】  
**Button()**: button=Button(tops,text="",frot=(,))【点击按钮】  
**StringVar()**: varl=StringVar()
**set**: varl=set("ready")  
**frame**：frame=tkinter.Frame（roo	t）【在根窗口中建立一个框架，之后建立的对象都在frame中，可以将对象进行分组】  
**pack**：frame.pack(side=BOTTOM)【包装】
**grid()**: text.grid(row=，column=，sticky=，columnspan=，rowspan=)
----------
布局器,将窗口分割为表格，在加入button、scrolledtext、label,需要将其在窗口中分别进行布局
pack（）和grid（）不能一起使用
在指定的row和column上放置对象，row和column仅指定起始位置  
columnspan和rowspan指定从起始位置开始，占用的行列数  
sticky有N/S/W/E(在指定的位置上下左右对齐)




