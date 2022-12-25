from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator=""
    text_input.set("")

def btnequalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

n=Tk()
text_input=StringVar()
operator=""
b1=Button(n,padx=9,bd=5,text="+",bg='blue',command=lambda:btnclick('+'),fg='yellow',font=('Arial',10,'bold'))
b1.place(x=220,y=250)
b2=Button(n,padx=10,bd=5,text="0",bg='grey',command=lambda:btnclick(0),fg='blue',font=('Arial',10,'bold'))
b2.place(x=15,y=250)

b20=Button(n,padx=10,bd=5,text=".",bg='grey',command=lambda:btnclick("."),fg='blue',font=('Arial',10,'bold'))
b20.place(x=85,y=250)

b3=Button(n,padx=11,bd=5,text="/",bg="blue",command=lambda:btnclick('/'),fg="yellow",font=('Arial',10,'bold'))
b3.place(x=220,y=100)

b5=Button(n,padx=9,bd=5,text="x",bg='blue',command=lambda:btnclick('*'),fg='yellow',font=('Arial',10,'bold'))
b5.place(x=220,y=150)
#===============================================================
b6=Button(n,padx=10,bd=5,text="7",bg='grey',command=lambda:btnclick(7),fg='blue',font=('Arial',10,'bold'))
b6.place(x=15,y=200)
b7=Button(n,padx=10,bd=5,text="8",bg='grey',command=lambda:btnclick(8),fg='blue',font=('Arial',10,'bold'))
b7.place(x=85,y=200)
b8=Button(n,padx=10,bd=5,text="9",bg="grey",command=lambda:btnclick(9),fg="blue",font=('Arial',10,'bold'))
b8.place(x=155,y=200)

#===============================================================
b10=Button(n,padx=10,bd=5,text="4",bg='grey',command=lambda:btnclick(4),fg='blue',font=('Arial',10,'bold'))
b10.place(x=15,y=150)
b11=Button(n,padx=10,bd=5,text="5",bg='grey',command=lambda:btnclick(5),fg='blue',font=('Arial',10,'bold'))
b11.place(x=85,y=150)
b12=Button(n,padx=10,bd=5,text="6",bg="grey",command=lambda:btnclick(6),fg="blue",font=('Arial',10,'bold'))
b12.place(x=155,y=150)
#==================================================================
b10=Button(n,padx=10,bd=5,text="1",bg='grey',command=lambda:btnclick(1),fg='blue',font=('Arial',10,'bold'))
b10.place(x=15,y=100)
b11=Button(n,padx=10,bd=5,text="2",bg='grey',command=lambda:btnclick(2),fg='blue',font=('Arial',10,'bold'))
b11.place(x=85,y=100)
b12=Button(n,padx=10,bd=5,text="3",bg="grey",command=lambda:btnclick(3),fg="blue",font=('Arial',10,'bold'))
b12.place(x=155,y=100)
b5=Button(n,padx=11,bd=5,text="-",bg='blue',command=lambda:btnclick('-'),fg='yellow',font=('Arial',10,'bold'))
b5.place(x=220,y=200)
b14=Button(n,padx=10,bd=5,text="=",bg='blue',fg='yellow',font=('Arial',10,'bold'),command=btnequalsinput)
b14.place(x=155,y=250)
b15=Button(n,padx=110,bd=4,text="Ac",bg='red',fg='yellow',font=('Arial',10,'bold'),command=btncleardisplay)
b15.place(x=15,y=65)


e1=Entry(n,font=('Arial',16,'bold'),textvariable=text_input,bd=20,insertwidth=0,bg="grey",justify='right').grid(columnspan=2)

n.title("Calculator_P&H")
n.geometry("280x300")
n.mainloop()




