from tkinter import *
def clickedbtn1():
    print("Hello")
def clickedbtn2():
    print("Hello")
def clickedbtn3():
    print("Hello")
def clickedbtn4():
    print("Hello")
def clickedbtn5():
    print("Hello")
window = Tk()
window.geometry('350x200')
window.title("Pharmacy Management Software")
lbl = Label(window, text="Welcome to Pharmacy Management Software!")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="What would you like to do!")
lbl2.grid(column=0, row=1)
btn1 = Button(window, text="Medicine Menu",fg="red", command=clickedbtn1)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Customer Menu",fg="red", command=clickedbtn2)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="Supplier Menu",fg="red", command=clickedbtn3)
btn3.grid(column=0, row=4)
btn4 = Button(window, text="Report Menu",fg="red", command=clickedbtn4)
btn4.grid(column=0, row=5)
btn5 = Button(window, text="Invoicing Menu",fg="red", command=clickedbtn5)
btn5.grid(column=0, row=6)
window.mainloop()

