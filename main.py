from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.configure(width=100, height=100, bg="black")

height = DoubleVar()
height_label = Label(root, text="Height", fg="red", bg="black", font=("Calibri 14 bold"),
                     pady=5, padx=8)
height_label.grid(row=2)

height_entry = Entry(root, textvariable=height)
height_entry.grid(row=2, column=1, columnspan=2, padx=5)


mass = DoubleVar()
mass_label = Label(root, text="Mass", fg="red", bg="black", font=("Calibri 14 bold"),
                     pady=10, padx=2)
mass_entry = Entry(root, textvariable=height)
mass_label.grid(row=4)
mass_entry.grid(row=4, column=1)


mainloop()