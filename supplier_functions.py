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
