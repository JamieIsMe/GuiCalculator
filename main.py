import tkinter as tk

# have to add a +/- button, will be an int either -1 or 1 and will mulliply the number by it

def add_character(character):
    global display_text
    global num_one
    global num_two
    global status
    global operation
    global result
    display_text += character
    if character.isnumeric() and status:
        if result != "":
            clear_calulator()
            display_text += character
        num_one += character
    elif character.isnumeric() and not status:
        num_two += character
    elif operation == "":
        if result != "":
            num_one = result
            display_text = num_one+character
            label_display.config(text=display_text)
        operation = character
        status = False
    if character == "=":
        if operation == "-":
            result = str(float(num_one) - float(num_two))
            display_text += result
        elif operation == "+":
            result = str(float(num_one) + float(num_two))
            display_text += result
        elif operation == "*":
            result = str(float(num_one) * float(num_two))
            display_text += result
        elif operation == "/":
            result = str(float(num_one) / float(num_two))
            display_text += result
        num_one = ""
        num_two = ""
        operation = ""
        status = True
    elif character == "C":
        clear_calulator()
    label_display.config(text=display_text)

def clear_calulator():
    global display_text
    global num_one
    global num_two
    global status
    global operation
    global result
    display_text = ""
    num_one = ""
    num_two = ""
    operation = ""
    result = ""
    status = True
    label_display.config(text=display_text)

def setup_button(number):
    return tk.Button(gui, text=number, command=lambda: add_character(number), height=3, width=5)

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Calculator App")
    gui.geometry("265x300")
    gui.resizable(False, False)
    display_text = ""
    label_display = tk.Label(gui)

    operation = ""
    num_one = ""
    num_two = ""
    status = True
    result = ""

    button_zero = setup_button("0")
    button_one = setup_button("1")
    button_two = setup_button("2")
    button_three = setup_button("3")
    button_four = setup_button("4")
    button_five = setup_button("5")
    button_six = setup_button("6")
    button_seven = setup_button("7")
    button_eight = setup_button("8")
    button_nine = setup_button("9")
    button_equal = setup_button("=")
    button_divide = setup_button("/")
    button_multipy = setup_button("*")
    button_subtract = setup_button("-")
    button_addition = setup_button("+")
    button_clear = setup_button("C")
    button_temp = setup_button("+/-")

    button_zero.place(x=10, y=230)
    button_one.place(x=10, y=170)
    button_two.place(x=60, y=170)
    button_three.place(x=110, y=170)
    button_four.place(x=10, y=110)
    button_five.place(x=60, y=110)
    button_six.place(x=110, y=110)
    button_seven.place(x=10, y=50)
    button_eight.place(x=60, y=50)
    button_nine.place(x=110, y=50)
    label_display.grid(row=0, column=0)

    button_equal.place(x=210, y=230)
    button_divide.place(x=160, y=110)
    button_multipy.place(x=160, y=170)
    button_subtract.place(x=110, y=230)
    button_addition.place(x=60, y=230)
    button_clear.place(x=160, y=50)
    button_temp.place(x=160, y=230)

    gui.mainloop()
