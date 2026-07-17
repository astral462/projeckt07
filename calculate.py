from customtkinter import *

def press(value):
    operators = "+-*/"
    current = entry.get()
    if value in operators and current:
        if current[-1] in operators:
            return

    entry.insert(END, value)

def calculator():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, result)

def clear():
    entry.delete(0, END)

window = CTk()
window.title("Калькулятор")
window.geometry("350x550")

entry = CTkEntry(window, width=300, height=50)
entry.grid(column=0, row=0, columnspan=4, pady=5)

btn_1 = CTkButton(window, text="1", width=70, height=50, command=lambda: press("1"))
btn_1.grid(column=0, row=3, pady=5, padx=5)

btn_2 = CTkButton(window, text="2", width=70, height=50, command=lambda: press("2"))
btn_2.grid(column=1, row=3, pady=5, padx=5)

btn_3 = CTkButton(window, text="+", width=70, height=50, command=lambda: press("+"))
btn_3.grid(column=1, row=4, pady=5, padx=5)

btn_4 = CTkButton(window, text="=", width=70, height=50, command=calculator)
btn_4.grid(column=3, row=4, pady=5, padx=5)

btn_5 = CTkButton(window, text="3", width=70, height=50, command=lambda: press("3"))
btn_5.grid(column=2, row=3, pady=5, padx=5)

btn_6 = CTkButton(window, text="4", width=70, height=50, command=lambda: press("4"))
btn_6.grid(column=0, row=2, pady=5, padx=5)

btn_7 = CTkButton(window, text="5", width=70, height=50, command=lambda: press("5"))
btn_7.grid(column=1, row=2, pady=5, padx=5)

btn_8 = CTkButton(window, text="6", width=70, height=50, command=lambda: press("6"))
btn_8.grid(column=2, row=2, pady=5, padx=5)

btn_9 = CTkButton(window, text="7", width=70, height=50, command=lambda: press("7"))
btn_9.grid(column=0, row=1, pady=5, padx=5)

btn_10 = CTkButton(window, text="8", width=70, height=50, command=lambda: press("8"))
btn_10.grid(column=1, row=1, pady=5, padx=5)

btn_11 = CTkButton(window, text="9", width=70, height=50, command=lambda: press("9"))
btn_11.grid(column=2, row=1, pady=5, padx=5)

btn_12 = CTkButton(window, text="0", width=70, height=50, command=lambda: press("0"))
btn_12.grid(column=0, row=4, pady=5, padx=5)

btn_13 = CTkButton(window, text="/", width=70, height=50, command=lambda: press("/"))
btn_13.grid(column=2, row=4, pady=5, padx=5)

btn_14 = CTkButton(window, text="-", width=70, height=50, command=lambda: press("-"))
btn_14.grid(column=3, row=3, pady=5, padx=5)

btn_15 = CTkButton(window, text="*", width=70, height=50, command=lambda: press("*"))
btn_15.grid(column=3, row=2, pady=5, padx=5)

btn_16 = CTkButton(window, text="|", width=70, height=50, command=clear)
btn_16.grid(column=3, row=1, pady=5, padx=5)


window.mainloop()
