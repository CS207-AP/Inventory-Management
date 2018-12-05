from tkinter import *
import menu_functions
import sys
#Medicine Menu
def clickedbtn1():
    medicine_menu_window = Tk()
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('350x200')
    

#Customer Menu
def clickedbtn2():
    print("Hello")
#Supplier Menu
def clickedbtn3():
    print("Hello")
#Report Menu
def clickedbtn4():
    print("Hello")
#Invoicing Menu
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
menu_choice=0
while menu_choice != 6:
    print ("Enter 1 for medicine menu. \nEnter 2 for customer menu. \nEnter 3 for supplier menu. \nEnter 4 for report menu. \nEnter 5 for Invoicing. \nEnter 6 to quit program.\n")
    menu_choice=int(input("Enter Your Choice!\n"))
    if menu_choice==1:
        menu_functions.medicine_menu()
    elif menu_choice==2:
        menu_functions.customer_menu()
    elif menu_choice==3:
        menu_functions.supplier_menu()
    elif menu_choice==4:
        menu_functions.report_menu()
    elif menu_choice==5:
        menu_functions.invoicing_menu()
    else:
        print("Invalid Input! Try Again! \n")    
sys.exit()

