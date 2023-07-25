from tkinter import *


def calc():
    BMI = BMI_val(mass.get(), height.get())
    Stat = get_status()
    stat.set(Stat)
    bmi_Val.set(format(BMI, '.2f'))

def BMI_val(mass, height):
    return mass / height ** 2

def get_height():
    return height

def clear():
    stat.set("")
    bmi_Val.set("0.0")
    mass_entry.delete(0, "end")
    height_entry.delete(0, "end")


def get_width():
    return mass

def get_status():
    if bmi_Val.get() > 40:
        return "You are obese class 3"
    elif bmi_Val.get() > 35 or bmi_Val.get() < 40:
        return "You are obese class 2"
    elif bmi_Val.get() > 30 or bmi_Val.get() < 35:
        return "You are obese class 1"
    elif bmi_Val.get() > 25 or bmi_Val.get() < 30:
        return "You are overweight"
    elif bmi_Val.get() > 18.5 or bmi_Val.get() < 25:
        return "You are normal"
    elif bmi_Val.get() > 17 or bmi_Val.get() < 18.5:
        return "You are thin"
    else:
        return "You are moderately thin"


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
mass_entry = Entry(root, textvariable=mass)
mass_label.grid(row=4)
mass_entry.grid(row=4, column=1)

bmi_Val = DoubleVar()
stat = StringVar()

bmi = Label(root, text="BMI: ", fg="blue", bg="black", font=("Calibri 14 bold"),
                    pady=10, padx=2, justify=LEFT)

status = Label(root, text="Status", fg="blue", bg="black", font=("Calibri 14 bold"),
                    pady=10, padx=2, justify=LEFT)

status_msg = Label(root, textvariable=stat, fg="white", bg="black", font=("Calibri 14 bold"),
                   pady=10, padx=2)

bmi_total = Label(root, textvariable=bmi_Val, fg="white", bg="black", font=("Calibri 14 bold"),
                   pady=10, padx=2)

bmi.grid(row=6)
status.grid(row=7)
bmi_total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

calculate = Button(root,text="Calculate", command=calc, fg="white", bg="black", font=("Calibri 14 bold"),
                   pady=10, padx=2)
clear_button = Button(root, text="Reset", command=clear, fg="black", bg="white", font=("Calibri 14 bold"),
                   pady=10, padx=2)
calculate.grid(row=8)
clear_button.grid(row=8, column=3)

root.mainloop()