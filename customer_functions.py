import csv
from tempfile import NamedTemporaryFile
import shutil

def customer_id_generator():
    with open('cus_men.csv','r') as csvfile:
        reader=csv.DictReader(csvfile)
        i=1
        for row in reader:
            if int(row['customer_id'])==i:
                i=i+1            
    return i

def new_customer():
    with open('cus_men.csv','a+') as csvfile:
        names=['customer_name','customer_id','customer_phone','customer_address']
        writer=csv.DictWriter(csvfile,fieldnames=names)
        writer.writeheader()
        customer_name=input('Enter the name of the customer : ')
        customer_id=customer_id_generator()
        print('Unique customer ID generated : ',customer_id)
        customer_phone=input('Enter the phone number of the customer : ')
        customer_address=input('Enter the address : ')
        writer.writerow({'customer_name':customer_name,'customer_id':customer_id,'customer_phone':customer_phone,"customer_address":customer_address})

def search_customer():    
    with open('cus_men.csv','r') as csvfile:
        name=input('Enter the name of customer:\n')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['customer_name']==name:
                print("------------------------------------------")
                print(" Name : ",row['customer_name'],'\n',"ID : ",row['customer_id'],'\n',"Phone : ",row['customer_phone'],'\n',"Address : ",row['customer_address'])
                print("------------------------------------------")
def update_customer_info():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    names=['customer_name','customer_id','customer_phone','customer_address']
    with open('cus_men.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()
        idno =input('Enter the id of the customer you want to modify!\n')
        for row in reader:
            if row['customer_id'] == idno:
                print('---------------------------------------------')
                print("|Enter 1 to change name                     |")
                print('---------------------------------------------')
                print('|Enter 2 to change phone number             |')
                print('---------------------------------------------')
                print('|Enter 3 to change address                  |')
                print('---------------------------------------------') 
                choice=int(input("Enter Your Choice!\n"))

                if(choice==1):
                    row['customer_name']=input("Enter the new name : ")

                elif(choice==2):
                    row['customer_phone']=input("Enter the new phone number : ")

                elif(choice==3):

                    row['customer_address']=input("Enter the new address : ")

            row = {'customer_name':row['customer_name'],'customer_id':row['customer_id'],'customer_phone':row['customer_phone'],"customer_address":row['customer_address']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'cus_men.csv')