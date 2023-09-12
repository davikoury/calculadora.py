from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('525x515')

number1 = ''
number2 = ''
division = FALSE
multiplication = FALSE
subtraction = FALSE
addition = FALSE

root.configure(background='#c8c8c8') 

e = Entry(root, borderwidth=6, relief=RIDGE, bg='#ffffff', font=('Arial', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    ipady=20,
    ipadx=3
)

def button_click(num):
    e.insert(END, num)

def button_division():
    global number1, division
    division = True
    number1 = e.get()
    e.delete(0, END)

def button_multiplication():
    global number1, multiplication
    multiplication = True
    number1 = e.get()
    e.delete(0, END)

def button_subtraction():
    global number1, subtraction
    subtraction = True
    number1 = e.get()
    e.delete(0, END)

def button_addition():
    global number1, addition
    addition = True
    number1 = e.get()
    e.delete(0, END)

def button_equal():
    global division, multiplication, subtraction, addition
    number2 = e.get()
    e.delete(0, END)
    if division:
        result = float(number1) / float(number2)
        if result.is_integer():
            e.insert(0, int(result))
        else:
            e.insert(0, "{:.1f}".format(result))
        division = False
    if multiplication:
        result = float(number1) * float(number2)
        if result.is_integer():
            e.insert(0, int(result))
        else:
            e.insert(0, "{:.1f}".format(result))
        multiplication = False
    if subtraction:
        result = float(number1) - float(number2)
        if result.is_integer():
            e.insert(0, int(result))
        else:
            e.insert(0, "{:.1f}".format(result))
        subtraction = False
    if addition:
        result = float(number1) + float(number2)
        if result.is_integer():
            e.insert(0, int(result))
        else:
            e.insert(0, "{:.1f}".format(result))
        addition = False

def button_clear():
    e.delete(0, END)

# Operators

division = Button(root,
                 text='÷',
                 padx=43,
                 pady=20,
                 command=button_division,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

division.grid(row=0, column=4)

multiplication = Button(root,
                 text='×',
                 padx=43,
                 pady=20,
                 command=button_multiplication,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

multiplication.grid(row=1, column=4)

subtraction = Button(root,
                 text='-',
                 padx=44.5,
                 pady=20,
                 command=button_subtraction,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

subtraction.grid(row=2, column=4)

addition = Button(root,
                 text='+',
                 padx=43,
                 pady=20,
                 command=button_addition,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

addition.grid(row=3, column=4)

clear = Button(root,
                 text='C',
                 padx=40,
                 pady=20,
                 command=button_clear,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

clear.grid(row=4, column=3)

equal = Button(root,
                 text='=',
                 padx=43,
                 pady=20,
                 command=button_equal,
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

equal.grid(row=4, column=4)

# Numbers

one = Button(root,
                 text='1',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(1),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

one.grid(row=3, column=1)

two = Button(root,
                 text='2',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(2),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

two.grid(row=3, column=2)

three = Button(root,
                 text='3',
                 padx=41,
                 pady=20,
                 command=lambda:button_click(3),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

three.grid(row=3, column=3)



four = Button(root,
                 text='4',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(4),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

four.grid(row=2, column=1)

five = Button(root,
                 text='5',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(5),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

five.grid(row=2, column=2)

six = Button(root,
                 text='6',
                 padx=41,
                 pady=20,
                 command=lambda:button_click(6),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

six.grid(row=2, column=3)



seven = Button(root,
                 text='7',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(7),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

seven.grid(row=1, column=1)

eight = Button(root,
                 text='8',
                 padx=40,
                 pady=20,
                 command=lambda:button_click(8),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

eight.grid(row=1, column=2)

nine = Button(root,
                 text='9',
                 padx=41,
                 pady=20,
                 command=lambda:button_click(9),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

nine.grid(row=1, column=3)



zero = Button(root,
                 text='0',
                 padx=105,
                 pady=20,
                 command=lambda:button_click(0),
                 fg='#000000',
                 bg='#ffffff',
                 bd=6,
                 relief='ridge',
                 font=('Arial', 20, 'bold')
)

zero.grid(row=4, column=1, columnspan=2)

root.mainloop()
