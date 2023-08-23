from tkinter import *

def button_convert():
    miles = float(input.get())
    output = round(miles * 1.609)
    km_output.config(text=f"{output}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column= 0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_convert)
calculate_button.grid(column=1, row=2)

window.mainloop()