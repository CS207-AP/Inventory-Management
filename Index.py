import menu_functions
import sys
menu_choice=0
while menu_choice != 6:
    print ("Enter 1 for medicine menu. \nEnter 2 for customer menu. \nEnter 3 for supplier menu. \nEnter 4 for report menu. \nEnter 5 for Invoicing. \nEnter 6 to quit program.\n")
    menu_choice=int(input("Enter Your Choice!\n"))
    if menu_choice==1:
        menu_functions.medicine_menu()
    else:
        print("Invalid Input! Try Again! \n")
    elif menu_choice==2:
        menu_functions.customer_menu()
    elif menu_choice==3:
        menu_functions.supplier_menu()
    elif menu_choice==4:
        menu_functions.report_menu()
    elif menu_choice==5:
        menu_functions.invoicing_menu()
sys.exit()