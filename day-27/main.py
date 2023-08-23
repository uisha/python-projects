from tkinter import *

window = Tk()
window.title("My First GUI Program With Tkinter")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Times New Roman", 24))
my_label.pack()

# Button
def button_clicked():
    my_label.config(text=input.get())

my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()