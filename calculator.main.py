from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("610x600+600+200") #width x(seprate width from height) height+Xposition+Yposition
window.resizable(False, False)# with this line of code user won't be able to change the size of window manually
window.configure(background="#17161b")
text_box = Entry(window, width=27, font=("arial", 30), bd=5)
text_box.place(x=1, y=20)


def insert(value):
    text_box.insert("end", value)
def clear():
    text_box.delete(0, "end")

def evaluate():
    try:
        result = eval(text_box.get())
        text_box.delete(0, "end")
        text_box.insert("end", str(result))
    except ZeroDivisionError:
        text_box.delete(0, "end")
        text_box.insert("end", "Error: Division by zero")
    except SyntaxError:
        text_box.delete(0, "end")
        text_box.insert("end", "Error: Invalid input")
    except Exception as e:
        text_box.delete(0, "end")
        text_box.insert("end", f"Error: {e}")


btn1 = Button(window, width=5, height=1, text="C", font=("arial", 30, "bold"), bd=5, background="#3697f5", fg="#fff",command=lambda :clear()).place(x=5, y=100) # if we don't put lambda here the function isn't excecute
btn2 =Button(window, width=5, height=1, text="/", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("/")).place(x=150, y=100)
btn3 =Button(window, width=5, height=1, text="%", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("%")).place(x=290, y=100)
btn4 =Button(window, width=5, height=1, text="*", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("*")).place(x=430, y=100)

btn5 =Button(window, width=5, height=1, text="7", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("7")).place(x=5, y=200)
btn6 =Button(window, width=5, height=1, text="8", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("8")).place(x=150, y=200)
btn7 =Button(window, width=5, height=1, text="9", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("9")).place(x=290, y=200)
btn8 =Button(window, width=5, height=1, text="-", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("-")).place(x=430, y=200)

btn9 =Button(window, width=5, height=1, text="4", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("4")).place(x=5, y=300)
btn10 =Button(window, width=5, height=1, text="5", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("5")).place(x=150, y=300)
btn11 =Button(window, width=5, height=1, text="6", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("6")).place(x=290, y=300)
btn12 =Button(window, width=5, height=1, text="+", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("+")).place(x=430, y=300)

btn13 =Button(window, width=5, height=1, text="1", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("1")).place(x=5, y=400)
btn14 =Button(window, width=5, height=1, text="2", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("2")).place(x=150, y=400)
btn15 =Button(window, width=5, height=1, text="3", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("3")).place(x=290, y=400)
btn16 =Button(window, width=11, height=1, text="0", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert("0")).place(x=10, y=500)

btn17 =Button(window, width=5, height=1, text=".", font=("arial", 30, "bold"), bd=5, background="#2a2d36", fg="#fff",command=lambda :insert(".")).place(x=290, y=500)
btn18 = (Button(window, width=5, height=5, text="=", font=("arial", 30, "bold"), bd=5, background="#fe9037", fg="#fff",command=lambda :evaluate())
         .place(x=430, y=400))

window.mainloop()
