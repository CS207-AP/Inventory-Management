import csv
from tempfile import NamedTemporaryFile
import shutil

def customer_id_generator():
    with open('cus_men.csv','r') as csvfile:
        reader=csv.DictReader(csvfile)
        i=1
        for row in reader:
            if int(row['Customer_ID'])==i:
                i=i+1            
    return i

def new_customer():
    
    with open('cus_men.csv','a+') as csvfile:
        names=['Customer_Name','Customer_ID','Customer_Phone','Customer_Medicine']
        writer=csv.DictWriter(csvfile,fieldnames=names)
        Customer_Name=input('Enter the name of the customer: ')
        Customer_ID=customer_id_generator()
        print('Unique customer ID generated: ',Customer_ID)
        Customer_Phone=input('Enter the phone number of the customer: ')
        Customer_Medicine=input('Enter the medicine that the customer needs: ')
        writer.writerow({'Customer_Name':Customer_Name,'Customer_ID':Customer_ID,'Customer_Phone':Customer_Phone,"Customer_Medicine":Customer_Medicine})

def search_customer():
    
    with open('cus_men.csv','r') as csvfile:
        no=input('Enter the id to search ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['Customer_ID']==no:
                print(row['Customer_Name'],row['Customer_ID'],row['Customer_Phone'],row['Customer_Medicine'])

def update_customer_info():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    names=['Customer_Name','Customer_ID','Customer_Phone','Customer_Medicine']
    with open('cus_men.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()
        idno =input('Enter the id of the customer you want to modify: ')
        for row in reader:
            if row['Customer_ID'] == idno:
                choice=int(input('1. To update the Name\n2. To update the phone number\n3. To update the medicine name\n'))

                if(choice==1):
                    row['Customer_Name']=input("Enter the new name: ")

                elif(choice==2):
                    row['Customer_Phone']=input("Enter the new phone number: ")

                elif(choice==3):
                    row['Customer_Medicine']=input("Enter the medicine name")



            row = {'Customer_Name':row['Customer_Name'],'Customer_ID':row['Customer_ID'],'Customer_Phone':row['Customer_Phone'],"Customer_Medicine":row['Customer_Medicine']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'cus_men.csv')
new_customer()