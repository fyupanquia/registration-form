from tkinter import * 
root = Tk()
root.geometry("500x300")


Label(root,text="Python registration form",font="ar 15 bold").grid(row=0, column=3)


name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmethod = Label(root, text="Payment method")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmethod.grid(row=5, column=2)

nameval = StringVar
phoneval = StringVar
genderval = StringVar
emergencyval = StringVar
paymentmethodval = StringVar
checkval = IntVar


nameEntry = Entry(root, textvariable=nameval)
phoneEntry = Entry(root, textvariable=phoneval)
genderEntry = Entry(root, textvariable=genderval)
paymentmethodEntry = Entry(root, textvariable=paymentmethodval)
emergencyEntry = Entry(root, textvariable=emergencyval)


nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyEntry.grid(row=4, column=3)
paymentmethodEntry.grid(row=5, column=3)


def getVals():
    print("submitted")

checkbtn = Checkbutton(text="remember me?", variable=checkval)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getVals).grid(row=7, column=3)


root.mainloop()