import csv
def create_supplier():
        with open('supplier.csv', 'a+') as csvfile:
                columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
                writer = csv.DictWriter(csvfile, fieldnames = columns)
                sup_name = input("Enter New Supplier's Name!\n")
                sup_id = int(input("Enter New Supplier's Id\n"))
                sup_city = input("Enter New Supplier's City!\n")
                sup_contact = int(input("Enter New Supplier's Contact Number!\n"))
                sup_email = input("Enter New Supplier's Email Id!\n")
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
                id=int(input('Enter Supplier Name!\n'))
                reader=csv.DictReader(csvfile)
                for r in reader:
                        if r['sup_id'] == id:
                                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
def search_supplier():
        ss_choice=0
        while(ss_choice!=3):
                print("Enter 1 to search supplier by name!\nEnter 2 to search supplier by id!\nEnter 3 to exit supplier search!\n")
                ss_choice=int(input("Enter your choice!\n"))
                if ss_choice==1 :
                        s_searchbyname()
                elif ss_choice==2 :
                        s_searchbyid()
                else:
                        print("Invalid Input! Try again!\n")
def update_supplier_info():
        print("TEST")