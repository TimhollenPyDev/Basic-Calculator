import tkinter

# Make the window
root = tkinter.Tk()
root.title("Calculator")
root.geometry("370x450")
root.resizable(height=False, width=False)

num1 = ""
num2 = ""
num_choice = 1
function_choice = 0


def B1():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "1"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "1"
        display.config(text=num2)


def B2():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "2"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "2"
        display.config(text=num2)


def B3():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "3"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "3"
        display.config(text=num2)


def B4():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "4"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "4"
        display.config(text=num2)


def B5():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "5"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "5"
        display.config(text=num2)


def B6():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "6"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "6"
        display.config(text=num2)


def B7():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "7"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "7"
        display.config(text=num2)


def B8():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "8"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "8"
        display.config(text=num2)


def B9():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "9"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "9"
        display.config(text=num2)


def B0():
    global num1, num_choice, num2
    if num_choice == 1:
        num1 += "0"
        display.config(text=num1)
    if num_choice == 2:
        num2 += "0"
        display.config(text=num2)


def add():
    global num1, num2, num_choice, function_choice

    num_choice = 2
    function_choice = 1
    display.config(text=" ")


def sub():
    global num1, num2, num_choice, function_choice
    num_choice = 2
    function_choice = 2
    display.config(text=" ")


def mult():
    global num1, num2, num_choice, function_choice
    num_choice = 2
    function_choice = 3
    display.config(text=" ")


def div():
    global num1, num2, num_choice, function_choice
    num_choice = 2
    function_choice = 4
    display.config(text=" ")


def equals():
    global num1, num2, num_choice, function_choice
    if function_choice == 1:
        num1 = int(num1) + int(num2)
        display.config(text=num1)
    if function_choice == 2:
        num1 = int(num1) - int(num2)
        display.config(text=num1)
    if function_choice == 3:
        num1 = int(num1) * int(num2)
        display.config(text=num1)
    if function_choice == 4:
        num1 = int(num1) // int(num2)
        display.config(text=num1)


# Now i will make the display

display = tkinter.Label(root, width=15, height=2)
display.config(bg="light grey", font="Sans 35", text="", anchor="w")
display.grid(row=1, column=1, columnspan=100)

# Now i will make the buttons

N1 = tkinter.Button(root, width=3, height=1)
N1.config(text="1", font="Sans 35", command=B1)
N1.grid(row=2, column=1)

N2 = tkinter.Button(root, width=3, height=1)
N2.config(text="2", font="Sans 35", command=B2)
N2.grid(row=2, column=2)

N3 = tkinter.Button(root, width=3, height=1)
N3.config(text="3", font="Sans 35", command=B3)
N3.grid(row=2, column=3)

N4 = tkinter.Button(root, width=3, height=1)
N4.config(text="4", font="Sans 35", command=B4)
N4.grid(row=3, column=1)

N5 = tkinter.Button(root, width=3, height=1)
N5.config(text="5", font="Sans 35", command=B5)
N5.grid(row=3, column=2)

N6 = tkinter.Button(root, width=3, height=1)
N6.config(text="6", font="Sans 35", command=B6)
N6.grid(row=3, column=3)

N7 = tkinter.Button(root, width=3, height=1)
N7.config(text="7", font="Sans 35", command=B7)
N7.grid(row=4, column=1)

N8 = tkinter.Button(root, width=3, height=1)
N8.config(text="8", font="Sans 35", command=B8)
N8.grid(row=4, column=2)

N9 = tkinter.Button(root, width=3, height=1)
N9.config(text="9", font="Sans 35", command=B9)
N9.grid(row=4, column=3)

N0 = tkinter.Button(root, width=6, height=1)
N0.config(text="0", font="Sans 37", anchor="n", command=B0)
N0.grid(row=5, column=1, sticky="w", columnspan=2)

equals_button = tkinter.Button(root, width=3, height=1)
equals_button.config(text="=", font="Sans 35", anchor="n", command=equals)
equals_button.grid(row=5, column=3, sticky="w")

mult_button = tkinter.Button(root, width=3, height=1)
mult_button.config(text="X", font="Sans 35", command=mult)
mult_button.grid(row=2, column=4)

div_button = tkinter.Button(root, width=3, height=1)
div_button.config(text="/", font="Sans 35", command=div)
div_button.grid(row=3, column=4)

add_button = tkinter.Button(root, width=3, height=1)
add_button.config(text="+", font="Sans 35", command=add)
add_button.grid(row=4, column=4)

sub_button = tkinter.Button(root, width=3, height=1)
sub_button.config(text="-", font="Sans 35", anchor="n", command=sub)
sub_button.grid(row=5, column=4)

root.mainloop()
