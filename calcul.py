import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

root = tk.Tk()

root.geometry("500x500")

root.title("GUInea")

label= tk.Label(root, text="CALCULATOR", font=('Arial',18))
label.pack(padx=20, pady=20)

text_result= tk.Text(root,height=3,font=('Arial',18))
text_result.pack(padx=10, pady=10)

buttonframe= tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1=tk.Button(buttonframe, text="1", command=lambda:add_to_calculation(1), font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2=tk.Button(buttonframe, text="2", command=lambda:add_to_calculation(2), font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3=tk.Button(buttonframe, text="3", command=lambda:add_to_calculation(3), font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4=tk.Button(buttonframe, text="4", command=lambda:add_to_calculation(4), font=('Arial', 18))
btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

btn5=tk.Button(buttonframe, text="5", command=lambda:add_to_calculation(5), font=('Arial', 18))
btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

btn6=tk.Button(buttonframe, text="6", command=lambda:add_to_calculation(6), font=('Arial', 18))
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

btn7=tk.Button(buttonframe, text="7", command=lambda:add_to_calculation(7), font=('Arial', 18))
btn7.grid(row=3, column=0, sticky=tk.W+tk.E)

btn8=tk.Button(buttonframe, text="8", command=lambda:add_to_calculation(8), font=('Arial', 18))
btn8.grid(row=3, column=1, sticky=tk.W+tk.E)

btn9=tk.Button(buttonframe, text="9", command=lambda:add_to_calculation(9), font=('Arial', 18))
btn9.grid(row=3, column=2, sticky=tk.W+tk.E)

btn0=tk.Button(buttonframe, text="0", command=lambda:add_to_calculation(0), font=('Arial', 18))
btn0.grid(row=4, column=1, sticky=tk.W+tk.E)

btn_C=tk.Button(buttonframe, text="C", command=clear_field, font=('Arial', 18))
btn_C.grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E)

btn_equal=tk.Button(buttonframe, text="=", command=evaluate_calculation, font=('Arial', 18))
btn_equal.grid(row=5, column=2, columnspan=2, sticky=tk.W+tk.E)

btn_plus=tk.Button(buttonframe, text="+", command=lambda:add_to_calculation("+"), font=('Arial', 18))
btn_plus.grid(row=0, column=3, sticky=tk.W+tk.E)

btn_minus=tk.Button(buttonframe, text="-", command=lambda:add_to_calculation("-"), font=('Arial', 18))
btn_minus.grid(row=2, column=3, sticky=tk.W+tk.E)

btn_mul=tk.Button(buttonframe, text="*", command=lambda:add_to_calculation("*"), font=('Arial', 18))
btn_mul.grid(row=3, column=3, sticky=tk.W+tk.E)

btn_div=tk.Button(buttonframe, text="/", command=lambda:add_to_calculation("/"), font=('Arial', 18))
btn_div.grid(row=4, column=3, sticky=tk.W+tk.E)

btn_open=tk.Button(buttonframe, text="(", command=lambda:add_to_calculation("("), font=('Arial', 18))
btn_open.grid(row=4, column=0, sticky=tk.W+tk.E)

btn_close=tk.Button(buttonframe, text=")", command=lambda:add_to_calculation(")"), font=('Arial', 18))
btn_close.grid(row=4, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')




root.mainloop()
