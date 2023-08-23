from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program With Tkinter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # adds padding

# Label
my_label = Label(text="I am a Label", font=("Times New Roman", 24))
my_label.grid(column=0, row=0)

# Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
window.mainloop()