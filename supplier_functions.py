import csv
from tempfile import NamedTemporaryFile
import shutil
def supplier_id_generator():
        with open('supplier.csv', 'r') as csvfile:
                reader=csv.DictReader(csvfile)
                i=1
                for r in reader:
                        if int(r['sup_id'])==i:
                                i=i+1
        return i
def create_supplier():
        with open('supplier.csv', 'a+') as csvfile:
                columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
                writer = csv.DictWriter(csvfile, fieldnames = columns)
                
                sup_name = input("Enter New Supplier's Name : ")
                sup_id = supplier_id_generator()
                print('Unique Supplier ID Generated : ', sup_id)
                sup_city = input("Enter New Supplier's City : ")
                sup_contact = int(input("Enter New Supplier's Contact Number : "))
                sup_email = input("Enter New Supplier's Email Id : ")
                writer.writerow({'sup_name':sup_name, 'sup_id':sup_id, 'sup_city':sup_city, 'sup_contact':sup_contact, 'sup_email':sup_email})
def s_searchbyname():
        with open('supplier.csv','r') as csvfile:
                name=input('Enter Supplier Name!\n')
                reader=csv.DictReader(csvfile)
                for r in reader:
                        if r['sup_name'] == name:
                                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
def s_searchbyid():
        with open('supplier.csv','r') as csvfile:
                id=int(input('Enter Supplier ID!\n'))
                reader=csv.DictReader(csvfile)
                for r in reader:
                        if r['sup_id'] == id:
                                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
def search_supplier():
        ss_choice=0
        while(ss_choice!=3):
                print('---------------------------------------------')
                print("|Enter 1 to search supplier by name!        |")
                print('---------------------------------------------')
                print("|Enter 2 to search supplier by id!          |")
                print('---------------------------------------------')
                print("|Enter 3 to exit supplier search!           |")
                print('---------------------------------------------')
                ss_choice=int(input("Enter your choice!\n"))
                if ss_choice==1 :
                        s_searchbyname()
                elif ss_choice==2 :
                        s_searchbyid()
                else:
                        print("Invalid Input! Try again!\n")
def update_supplier_info():
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
        with open('supplier.csv', 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile)
                writer = csv.DictWriter(tempfile, fieldnames=columns)
                writer.writeheader()
                suppp_name=input('Enter the name of the supplier you want to modify!\n')
                for r in reader:
                        if r['sup_name'] == suppp_name:
                                print('---------------------------------------------')
                                print('|Enter 1 to update supplier name.           |')
                                print('---------------------------------------------')
                                print('|Enter 2 to update supplier id.             |')
                                print('---------------------------------------------')
                                print('|Enter 3 to update supplier city.           |')
                                print('---------------------------------------------')
                                print('|Enter 4 to update supplier contact no.     |')
                                print('---------------------------------------------')
                                print('|Enter 5 to update supplier email id.       |')
                                print('---------------------------------------------')
                                choice=int(input('Enter your choice!\n'))
                                if(choice==1):
                                        r['sup_name']=input("Enter updated name : ")
                                elif(choice==2):
                                        r['sup_id']=int(input("Enter updated id : "))
                                elif(choice==3):
                                        r['sup_city']=input("Enter updated city : ")
                                elif(choice==4):
                                        r['sup_contact']=int(input("Enter updated contact : "))
                                elif(choice==5):
                                        r['sup_email']=int(input("Enter updated email id : "))
                                else:
                                        print("Invalid Input!\n")
                        r = {'sup_name':r['sup_name'], 'sup_id':r['sup_id'], 'sup_city':r['sup_city'], 'sup_contact':r['sup_contact'], 'sup_email':r['sup_email']}
                        writer.writerow(r)
        shutil.move(tempfile.name, 'supplier.csv')