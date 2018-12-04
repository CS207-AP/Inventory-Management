import medicine_functions
import customer_functions
import supplier_functions
import report_functions
import invoicing_functions
def medicine_menu():
    m_menu_choice=0
    while(m_menu_choice!=5):
        print("Enter 1 to search medicine. \nEnter 2 to add medicine. \nEnter 3 to update inventory . \nEnter 4 for Medicines to be purchased list. \nEnter 5 to to go back to Main Menu.\n")
        m_menu_choice=input()
        if(m_menu_choice==1):
            medicine_functions.search_medicine()
        elif(m_menu_choice==2):
            medicine_functions.add_medicine()
        elif(m_menu_choice==3):
            medicine_functions.update_medicine()
        elif(m_menu_choice==4):
            medicine_functions.medicine_to_be_purchased()
        else:
            print("Invalid Input! Try Again!\n")
def customer_menu():
    c_menu_choice=0
    while(c_menu_choice!=4):
        print("Enter 1 to search customer. \nEnter 2 to create new customer. \nEnter 3 to update customer information. \nEnter 4 to go back to Main Menu.\n")
        c_menu_choice=input()
        if(c_menu_choice==1):
           customer_functions.search_customer()
        elif(c_menu_choice==2):
            customer_functions.create_customer()
        elif(c_menu_choice==3):
            customer_functions.update_customer_info()
        else:
            print("Invalid Input! Try Again!\n")
def supplier_menu():
    s_menu_choice=0
    while(s_menu_choice!=4):
        print("Enter 1 to search supplier. \nEnter 2 to create new supplier. \nEnter 3 to update supplier information. \nEnter 4 to go back to Main Menu.")
        s_menu_choice=input()
        if(s_menu_choice==1):
            supplier_functions.search_supplier()
        elif(s_menu_choice==2):
            supplier_functions.create_supplier()
        elif(s_menu_choice==3):
            supplier_functions.update_supplier_info()
        else:
            print("Invalid Input! Try Again!\n")
def report_menu():
    r_menu_choice=0
    while(r_menu_choice!=6):
        print("Enter 1 for Todays sales. \n Enter 2 for this months sales. \n Enter 3 for todays purchases. \n Enter 4 for this months purchases. \n Enter 5 for profit report. \n Enter 6 to go back to main menu.")
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
        else:
            print("Invalid Input! Try Again!\n")
def invoicing_menu():
    invoicing_functions.invoice()