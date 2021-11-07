import random
import time
import tkinter
import string
import threading


root = tkinter.Tk()
root.title("Speed typing test")
root.attributes('-fullscreen', True)
root.config(bg="#000f09")


def quit():
    root.destroy()


def start():
    global char_list
    char_list = []
    for x in range(5):
        char_list.append(random.choice(string.ascii_lowercase))
    display.config(text=char_list[0])


def play_loop(self):
    try:
        if char_list[0] == entry_field.get():
            entry_field.delete(0)
            char_list.pop(0)
            display.config(text=char_list[0])

    except:
        IndexError()
        display.config(text="Du vann")

    finally:
        pass


start_lable = tkinter.Label(root, fg="#5c9c80", bg="#000f09", text="Speed typing test", font="sans 80", height=1,
                            width=14, )
start_lable.place(x=800, y=25)

display = tkinter.Label(root, fg="#5c9c80", text="Good luck", font="sans 80", height=1, width=14, bg="#000f09")
display.place(x=800, y=500)

exit_button = tkinter.Button(root, fg="#5c9c80", bg="#000f09", text="Exit ", font="sans 80", height=1, width=4,
                             activebackground="#000f09", activeforeground="#5c9c80", relief="flat", bd=0,
                             justify="left", command=quit)
exit_button.place(x=0, y=1240)

start_button = tkinter.Button(root, fg="#5c9c80", bg="#000f09", text="Start", font="sans 80", height=1, width=4,
                              activebackground="#000f09", activeforeground="#5c9c80", relief="flat", bd=0,
                              justify="left", command=start)
start_button.place(x=0, y=1090)

entry_field = tkinter.Entry(root, font="sans 80", fg="#5c9c80", bg="#000f09", relief="sunken", width=15,
                            justify="center")
entry_field.place(x=800, y=650)

tid_lable = tkinter.Label(root, fg="#5c9c80", bg="#000f09", text="Time: ", font="sans 80", height=1,
                            width=5, )
tid_lable.place(x=0, y=0)


root.bind("<Return>", play_loop)
root.mainloop()
