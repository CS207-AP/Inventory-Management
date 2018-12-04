def new_customer():
    import csv
    with open('cus_men.csv','a+') as csvfile:
        names=['Customer_Name','Customer_ID','Customer_Phone','Customer_Medicine']
        writer=csv.DictWriter(csvfile,fieldnames=names)
        Customer_Name=input('Enter the name of the customer: ')
        Customer_ID=input('Enter the customer ID: ')
        Customer_Phone=int(input('Enter the phone number of the customer: '))
        Customer_Medicine=input('Enter the medicine that the customer needs: ')
        writer.writerow({'Customer_Name':Customer_Name,'Customer_ID':Customer_ID,'Customer_Phone':Customer_Phone,"Customer_Medicine":Customer_Medicine})

def customer_search():
    import csv
    with open('cus_men.csv','r') as csvfile:
        no=input('Enter the id to search ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['Customer_ID']==no:
                print(row['Customer_Name'],row['Customer_ID'],row['Customer_Phone'],row['Customer_Medicine'])

def customer_update():

