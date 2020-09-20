
from tkinter import *

root = Tk()
def getvals():
    print("Submitting Form")
    
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")
    

    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")


root.geometry("644x344")

#Heading
Label(root, text= "Welcome To Pranav Travels", padx= 25,  font= "comicsansms 13 bold").grid(row= 0, column= 1)

#Text for our forms
name =Label(root, text= "Name")
phone=Label(root, text= "Phone")
gender=Label(root, text= "Gender")
emergency=Label(root, text= "Emergency Contact")
paymentmode=Label(root, text= "Payment Mode")

# Pack Text for our forms
name.grid(row= 1, column= 0)
phone.grid(row= 2, column= 0)
gender.grid(row= 3, column= 0)
emergency.grid(row= 4, column= 0)
paymentmode.grid(row= 5, column= 0)

#tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue= StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#entry for a form
nameentry = Entry(root, textvariable= namevalue)
phoneentry = Entry(root, textvariable= phonevalue)
genderentry = Entry(root, textvariable= gendervalue)
emergencyentry = Entry(root, textvariable= emergencyvalue)
paymentmodeentry = Entry(root, textvariable= paymentmodevalue)

#packing the entries
nameentry.grid(row= 1, column= 1)
phoneentry.grid(row= 2, column= 1)
genderentry.grid(row= 3, column= 1)
emergencyentry.grid(row= 4, column= 1)
paymentmodeentry.grid(row= 5, column= 1)

#checkbutton
foodservice = Checkbutton(text= "want to prebook your meal", variable = foodservicevalue)
foodservice.grid(row= 6, column= 1)

#Button and packing it and assigning it a command
Button(text = "Submit To Pranav Travels", command= getvals).grid(row= 7, column= 1)


root.mainloop()


