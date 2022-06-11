#Accessing the tkinter library
from tkinter import *
cr= Tk()

#placing the title, icon, size, and background color
cr.title("CR Simple Calculator")
cr.iconbitmap("calc.ico")
cr.geometry("384x385")
cr.configure(bg="black")

#Placing the entry box
e= Entry (cr,width=55, borderwidth= 5)
e.grid(row= 0, column=0, columnspan= 5, padx= 10, pady= 10)

#Assigning the functions for the calculator operation
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "add"
    f_num = int(first_number) #entry box maa string ko form maa hunxa tesaile operation garna ko lagi we have to change them into integer
    e.delete(0,END)
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)
def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0, END)
def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)
def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "pow"
    f_num = int(first_number)
    e.delete(0, END)
def button_per():
    first_number = e.get()
    global f_num
    global math
    math = "per"
    f_num = int(first_number)
    e.delete(0, END)
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add": 
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mul":
        e.insert(0, f_num * int(second_number))
    elif math == "div":
        e.insert (0, f_num / int(second_number))
    elif math == "pow":
        e.insert (0, f_num ** int(second_number))
    elif math == "per":
        e.insert (0, f_num % int(second_number))

#Defining the buttons
button_1 = Button(cr, text= "1",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(cr, text= "2",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(cr, text= "3",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(3))
button_3.grid(row=3, column=2)
button_4 = Button(cr, text= "4",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(cr, text= "5",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(cr, text= "6",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(cr, text= "7",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(cr, text= "8",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(cr, text= "9",bg= "grey20", fg = "white", padx = 40, pady= 20, command=lambda : button_click(9))
button_9.grid(row=1, column=2)
button_0 = Button(cr, text= "0",bg= "grey20", fg = "white", padx = 89, pady= 23, command=lambda : button_click(0))
button_0.grid(row=4, column=0, columnspan= 2)
button_add = Button(cr, text = "+",font= 100, bg="grey",fg= "black", padx= 37, pady= 18, command= button_add)
button_add.grid(row=2, column=4)
button_sub = Button(cr, text = "-",font= 90, bg= "grey",fg= "black", padx= 39, pady= 18, command= button_sub)
button_sub.grid(row=3, column=4)
button_mul = Button(cr, text = "×",font= 100, bg= "grey",fg= "black", padx= 37, pady= 20, command= button_mul)
button_mul.grid(row=4, column=4)
button_div = Button(cr, text = "÷",font= 95, bg= "grey",fg= "black", padx= 37, pady= 20, command= button_div)
button_div.grid(row=5, column=4)
button_pow = Button(cr, text = "^",font= 99, bg= "grey",fg= "black", padx= 38, pady= 20, command= button_pow)
button_pow.grid(row=5, column=2)
button_per = Button(cr, text = "%",font= 90, bg= "grey",fg= "black", padx= 35, pady= 20, command= button_per)
button_per.grid(row=4, column=2)
button_equal = Button(cr, text= "=",font= 50, bg="lightblue",fg= "black", padx = 86, pady= 20, command=button_equal)
button_equal.grid(row=5, column=0, columnspan = 2)
button_clear = Button(cr, text= "C",bg= "red", fg= "white", padx =39, pady= 20, command=button_clear)
button_clear.grid(row=1, column=4)

cr.mainloop()