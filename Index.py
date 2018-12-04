import menu_functions
menu_choice=0
while menu_choice != 6:
    print ("Enter 1 for medicine menu. \n Enter 2 for customer menu. \n Enter 3 for supplier menu. \n Enter 4 for report menu. \n Enter 5 for Invoicing. \n Enter 6 to quit program.\n")
    if(menu_choice==1):
        menu_functions.medicine_menu()
    elif(menu_choice==2):
        menu_functions.customer_menu()
    elif(menu_choice==3):
        menu_functions.supplier_menu()
    elif(menu_choice==4):
        menu_functions.report_menu()
    elif(menu_choice==5):
        menu_functions.invoicing_menu()
    else:
        print("Invalid Input! Try Again! \n")
