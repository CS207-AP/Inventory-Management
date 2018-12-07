import medicine_functions
import customer_functions
import supplier_functions
import report_functions
import invoicing_functions
def medicine_menu():
    m_menu_choice=0
    while(m_menu_choice!=5):
        print('---------------------------------------------')
        print("|Enter 1 to add medicine                    |")
        print('---------------------------------------------')
        print('|Enter 2 to search medicine                 |')
        print('---------------------------------------------')
        print('|Enter 3 to update medicine info            |')
        print('---------------------------------------------') 
        print('|Enter 4 for medicines to be purchased list |')
        print('---------------------------------------------')
        print('|Enter 5 to go back to Main Menu            |')
        print('---------------------------------------------')
        m_menu_choice=int(input("Enter Your Choice!\n"))
        if(m_menu_choice==1):
            medicine_functions.add_medicine()
        elif(m_menu_choice==2):
            medicine_functions.search_medicine()
        elif(m_menu_choice==3):
            medicine_functions.update_medicine()
        elif(m_menu_choice==4):
            medicine_functions.medicine_to_be_purchased()
        elif m_menu_choice==5:
            break
        else:
            print("Invalid Input! Try Again!\n")
def customer_menu():
    c_menu_choice=0
    while(c_menu_choice!=4):
        print('----------------------------------')
        print("|Enter 1 to search customer      |")
        print('----------------------------------')
        print('|Enter 2 to create new customer  |')
        print('----------------------------------')
        print('|Enter 3 to update customer info |')
        print('----------------------------------') 
        print('|Enter 4 to go back to main menu |')
        print('----------------------------------')
        c_menu_choice=int(input("Enter Your Choice!\n"))
        if(c_menu_choice==1):
           customer_functions.search_customer()
        elif(c_menu_choice==2):
            customer_functions.new_customer()
        elif(c_menu_choice==3):
            customer_functions.update_customer_info()
        elif c_menu_choice==4:
            break
        else:
            print("Invalid Input! Try Again!\n")
def supplier_menu():
    s_menu_choice=0
    while(s_menu_choice!=4):
        print('----------------------------------')
        print("|Enter 1 to search supplier      |")
        print('----------------------------------')
        print('|Enter 2 to create new supplier  |')
        print('----------------------------------')
        print('|Enter 3 to update supplier info |')
        print('----------------------------------') 
        print('|Enter 4 to go back to main menu |')
        print('----------------------------------')
        print("Enter 1 to search supplier. \nEnter 2 to create new supplier. \nEnter 3 to update supplier information. \nEnter 4 to go back to Main Menu.")
        s_menu_choice=int(input("Enter Your Choice!\n"))
        if(s_menu_choice==1):
            supplier_functions.search_supplier()
        elif(s_menu_choice==2):
            supplier_functions.create_supplier()
        elif(s_menu_choice==3):
            supplier_functions.update_supplier_info()
        elif s_menu_choice==4:
            break
        else:
            print("Invalid Input! Try Again!\n")
def report_menu():
    r_menu_choice=0
    while(r_menu_choice!=6):
        print('--------------------------------')
        print("|Enter 1 for today's sale      |")
        print('--------------------------------')
        print('|Enter 2 for monthly sale      |')
        print('--------------------------------')
        print("|Enter 3 for today's purchases |")
        print('--------------------------------') 
        print("|Enter 4 for monthly purchases |")
        print('--------------------------------')
        print('|Enter 5 for profit report     |')
        print('--------------------------------')
        print('|Enter 6 to go to main menu    |')
        print('--------------------------------')
    
        r_menu_choice=int(input("Enter Your Choice!\n"))
        if(r_menu_choice==1):
            report_functions.day_sale()
        elif(r_menu_choice==2):
            report_functions.month_sale()
        elif(r_menu_choice==3):
            report_functions.day_purchase()
        elif(r_menu_choice==4):
            report_functions.month_purchase()
        elif(r_menu_choice==5):
            report_functions.profit_report()
        elif r_menu_choice==6:
            break
        else:
            print("Invalid Input! Try Again!\n")
def invoicing_menu():
    i_menu_choice=0
    while(i_menu_choice!=3):
        print('---------------------------------')
        print("|Enter 1 for supplier invoice   |")
        print('---------------------------------')
        print('|Enter 2 for customer invoice   |')
        print('---------------------------------')
        print("|Enter 3 to return to main menu |")
        print('---------------------------------') 
        i_menu_choice=int(input("Enter Your Choice!\n"))
        if(i_menu_choice==1):
            invoicing_functions.sup_invoice()
        elif(i_menu_choice==2):
            invoicing_functions.cust_invoice()
        elif i_menu_choice==3:
            break
        else:
            print("Invalid Input! Try Again!\n")