'''
This module prints invoices
'''

import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime

D = datetime.datetime.now()
DATE = D.strftime("%d")
MONTH = D.strftime("%m")
YEAR = D.strftime("%Y")

def sup_invoice():
    '''
    This function prints supplier invoice
    '''
    medi_name = input("Enter medicine name : ")
    quantity = int(input("Enter quantity : "))
    sup_id = input("Enter supplier id : ")

    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open('medicine.csv', 'r+') as csvfile, open('medicine.csv', 'r+') as tempfile:
        columns = ['medi_name', 'med_id', 'sale', 'unit', 'quantity', 'min_quantity', \
                   'comp_name', 'sup_id', 'to_pur']
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()

        for row in reader:
            if row['medi_name'] == medi_name:
                med_id = row['med_id']
                unit = float(row['unit'])
                row['quantity'] = int(row['quantity']) + quantity
                if int(row['quantity']) < int(row['min_quantity']):
                    row['to_pur'] = int(row['min_quantity']) -int(row['quantity'])
                else:
                    row['to_pur'] = 0
            row_write = {'medi_name':row['medi_name'], 'med_id':row['med_id'], 'sale':row['sale'], \
                   'unit':row['unit'], 'quantity':row['quantity'], \
                   'min_quantity':row['min_quantity'], 'comp_name':row['comp_name'], \
                   'sup_id':row['sup_id'], 'to_pur':row['to_pur']}
            writer.writerow(row_write)

    cost = quantity * unit

    with open('purchase.csv', 'a+') as csvfile:
        columns = ['medi_name', 'med_id', 'unit', 'quantity', \
                   'pur_date', 'pur_month', 'pur_year', 'sup_id', 'cost']
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writerow({'medi_name':medi_name, 'med_id':med_id, 'unit':unit, \
                         'quantity':quantity, 'pur_date':DATE, 'pur_month':MONTH, \
                         'pur_year':YEAR, 'sup_id':sup_id, 'cost':cost})

    shutil.move(tempfile.name, 'medicine.csv')


def cust_invoice():
    '''
    This function prints customer invoice
    '''
    i = False
    medicinename = []
    medicinecost = []
    medicinequantity = []

    while i is not True:
        medi_name = input("Enter medicine name : ")
        customer_id = 0
        sale = 0.0
        total = 0.0
        quantity = int(input("Enter quantity : "))
        customer_name = input("Enter name of customer : ")

        with open('cus_men.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['customer_name'] == customer_name:
                    customer_id = row['customer_id']
        total = 0
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open('medicine.csv', 'r+') as csvfile, open('medicine.csv', 'r+') as tempfile:
            columns = ['medi_name', 'med_id', 'sale', 'unit', 'quantity', 'min_quantity', \
                       'comp_name', 'sup_id', 'to_pur']
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile, fieldnames=columns)
            writer.writeheader()

            for row in reader:
                if row['medi_name'] == medi_name:
                    med_id = row['med_id']
                    sale = float(row['sale'])
                    medicinename.append(medi_name)
                    medicinecost.append(sale)
                    medicinequantity.append(quantity)
                    total = quantity * sale
                    if quantity <= int(row['quantity']):
                        row['quantity'] = int(row['quantity']) - quantity
                    else:
                        print("Only", int(row['quantity']), "remaining in stock")
                        break
                    if int(row['quantity']) < int(row['min_quantity']):
                        row['to_pur'] = int(row['min_quantity']) -int(row['quantity'])
                    else:
                        row['to_pur'] = 0
                row_write = {'medi_name':row['medi_name'], 'med_id':row['med_id'], \
                             'sale':row['sale'], 'unit':row['unit'], 'quantity':row['quantity'],\
                             'min_quantity':row['min_quantity'], 'comp_name':row['comp_name'], \
                             'sup_id':row['sup_id'], 'to_pur':row['to_pur']}
                writer.writerow(row_write)
        shutil.move(tempfile.name, 'medicine.csv')

        with open('sales.csv', 'a+') as csvfile:
            columns = ['medi_name', 'med_id', 'sale', 'quantity', 'sale_date', 'sale_month', \
                       'sale_year', 'customer_name', 'customer_id', 'total']
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writerow({'medi_name':medi_name, 'med_id':med_id, 'sale':sale, \
                             'quantity':quantity, 'sale_date':DATE, 'sale_month':MONTH, \
                             'sale_year':YEAR, 'customer_name':customer_name, \
                             'customer_id':customer_id, 'total':total})

        print("Enter 0 for purchasing another medicine\nEnter 1 to print bill\n")
        i = bool(int(input()))

    print("|======Generating invoice======|\n")
    print("Ashoka Pharmacy\n")
    print("Date:", D.strftime("%x"))
    print("Time:", D.strftime("%X"))
    print("Customer:", customer_name)
    print("ID:", customer_id)
    print("|Name======quantity=price=total|")
    no_of_medicines = len(medicinename)
    for x_index in range(no_of_medicines):
        print("|", medicinename[x_index], "|", medicinequantity[x_index], "|", \
              medicinecost[x_index], "|", medicinequantity[x_index] * medicinecost[x_index])
    print("|==============================|")
    print("|Grand Total===================|")
    grandtotal = 0
    for x_index in range(no_of_medicines):
        grandtotal += medicinequantity[x_index] * medicinecost[x_index]
    print("Rs.", grandtotal)
    print("|==========Thank You!==========|")
