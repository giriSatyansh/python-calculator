from tkinter import *
root=Tk()
root.title("simple calculator")
e=Entry(root,bg="yellow",borderwidth=5,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(x):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(x))
def clear():
    e.delete(0,END)
def add():
     firstnumber=e.get()
     global f_num
     global math
     math="addition"
     f_num=int(firstnumber)
     e.delete(0,END)
def equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_num))
    if math=="subtraction":
        e.insert(0,f_num-int(second_num))
    if math=="multiplication":
        e.insert(0,f_num*int(second_num))
    if math=="division":
        e.insert(0,f_num/int(second_num))
    
def sub():
    firstnumber=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(firstnumber)
    e.delete(0,END)
    
def multi():
     firstnumber=e.get()
     global f_num
     global math
     math="multiplication"
     f_num=int(firstnumber)
     e.delete(0,END)
    
def div():
     firstnumber=e.get()
     global f_num
     global math
     math="division"
     f_num=int(firstnumber)
     e.delete(0,END)
button1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9))
button10=Button(root,text="0",padx=40,pady=20,command=lambda:click(0))
buttonadd=Button(root,text="+",padx=39,pady=20,command=add)
buttonequal=Button(root,text="=",padx=91,pady=20,command=equal)
buttonclear=Button(root,text="Clear",padx=79,pady=20,command=clear)
buttonsub=Button(root,text="-",padx=41,pady=20,command=sub)
buttonmulti=Button(root,text="*",padx=40,pady=20,command=multi)
buttondiv=Button(root,text="/",padx=41,pady=20,command=div)
button1.grid(row=3 ,column=0)
button2.grid(row=3 ,column=1)
button3.grid(row=3 ,column=2)
button4.grid(row=2 ,column=0)
button5.grid(row=2 ,column=1)
button6.grid(row=2 ,column=2)
button7.grid(row=1 ,column=0)
button8.grid(row=1 ,column=1)
button9.grid(row=1 ,column=2)
button10.grid(row=4 ,column=0)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonsub.grid(row=6,column=0)
buttonmulti.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)
root.mainloop()
