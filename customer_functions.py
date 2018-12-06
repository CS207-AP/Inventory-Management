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
        names=['customer_name','customer_id','customer_phone','customer_medicine']
        writer=csv.DictWriter(csvfile,fieldnames=names)
        customer_name=input('Enter the name of the customer: ')
        customer_id=customer_id_generator()
        print('Unique customer ID generated: ',customer_id)
        customer_phone=input('Enter the phone number of the customer: ')
        customer_medicine=input('Enter the medicine that the customer needs: ')
        writer.writerow({'customer_name':customer_name,'customer_id':customer_id,'customer_phone':customer_phone,"customer_medicine":customer_medicine})

def search_customer():    
    with open('cus_men.csv','r') as csvfile:
        no=input('Enter the id to search ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['customer_id']==no:
                print(row['customer_name'],row['customer_id'],row['customer_phone'],row['customer_medicine'])

def update_customer_info():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    names=['customer_name','customer_id','customer_phone','customer_medicine']
    with open('cus_men.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()
        idno =input('Enter the id of the customer you want to modify: ')
        for row in reader:
            if row['customer_id'] == idno:
                choice=int(input('1. To update the Name\n2. To update the phone number\n3. To update the medicine name\n'))

                if(choice==1):
                    row['customer_name']=input("Enter the new name: ")

                elif(choice==2):
                    row['customer_phone']=input("Enter the new phone number: ")

                elif(choice==3):

                    row['customer_medicine']=input("Enter the medicine name")

            row = {'customer_name':row['customer_name'],'customer_id':row['customer_id'],'customer_phone':row['customer_phone'],"customer_medicine":row['customer_medicine']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'cus_men.csv')

