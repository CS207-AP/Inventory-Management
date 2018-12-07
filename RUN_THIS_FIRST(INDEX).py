import menu_functions
import sys
menu_choice=0
while menu_choice != 6:
    print('-----------------------------')
    print("|Enter 1 for medicine menu  |")
    print('----------------------------')
    print('|Enter 2 for customer menu  |')
    print('----------------------------')
    print('|Enter 3 for supplier menu  |')
    print('----------------------------') 
    print('|Enter 4 for report menu    |')
    print('----------------------------')
    print('|Enter 5 for invoicing      |')
    print('----------------------------')
    print('|Enter 6 to quit the program|')
    print('-----------------------------')
    menu_choice=int(input("Enter Your Choice\n"))
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
    elif menu_choice==6:
        break
    else:
        print("Invalid Input! Try Again! \n")    
sys.exit()
