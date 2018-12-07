import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()
date= d.strftime("%d")
month= d.strftime("%m")
year = d.strftime("%Y")

def day_sale():
    print('Enter Date : ')
    date = input()
    print('Enter Month : ')
    month = input()
    print('Enter Year : ')
    year = input()
    count=0.0
    with open('sales.csv','r+') as csvfile:
        reader = csv.DictReader(csvfile)
        print('-----------------Day\'s Sales-----------------')
        for r in reader:
            if r['sale_date']==date and r['sale_month']==month and r['sale_year']==year :
                count=count+float(r['total'])
                print('Medicine Name : ', r['medi_name'])
                print('Medicine Id : ', r['med_id'])
                print('Sale : ', r['sale'])
                print('Quantity : ', r['quantity'])
                print('Total : ', r['total'])
                print('\n')
        print('-----------------------------------------------')
        print('Total sales for the day : ', count)
        print('-----------------------------------------------')
def month_sale():
    print('Enter Month : ')
    month = input()
    print('Enter Year : ')
    year = input()
    count=0.0
    with open('sales.csv','r+') as csvfile:
        reader = csv.DictReader(csvfile)
        print('-----------------Day\'s Sales-----------------')
        for r in reader:
            if r['sale_month']==month and r['sale_year']==year :
                count=count+float(r['total'])
                print('Medicine Name : ', r['medi_name'])
                print('Medicine Id : ', r['med_id'])
                print('Sale : ', r['sale'])
                print('Quantity : ', r['quantity'])
                print('Total : ', r['total'])
                print('\n')
        print('-----------------------------------------------')
        print('Total sales for the month : ', count)
        print('-----------------------------------------------')
def day_purchase():
    print('Enter Date : ')
    date = input()
    print('Enter Month : ')
    month = input()
    print('Enter Year : ')
    year = input()
    count=0.0
    with open('purchase.csv','r+') as csvfile:
        reader = csv.DictReader(csvfile)
        print('-----------------Day\'s Purchase-----------------')
        for r in reader:
            if r['pur_date']==date and r['pur_month']==month and r['pur_year']==year :
                count=count+float(r['total'])
                print('Medicine Name : ', r['medi_name'])
                print('Medicine Id : ', r['med_id'])
                print('Purchase cost per item : ', r['unit'])
                print('Quantity : ', r['quantity'])
                print('Total : ', r['cost'])
                print('\n')
        print('-----------------------------------------------')
        print('Total Purchase cost for the day : ', count)
        print('-----------------------------------------------')
def month_purchase():
    print('Enter Month : ')
    month = input()
    print('Enter Year : ')
    year = input()
    count=0.0
    with open('purchase.csv','r+') as csvfile:
        reader = csv.DictReader(csvfile)
        print('-----------------Day\'s Purchase-----------------')
        for r in reader:
            if r['pur_month']==month and r['pur_year']==year :
                count=count+float(r['total'])
                print('Medicine Name : ', r['medi_name'])
                print('Medicine Id : ', r['med_id'])
                print('Purchase cost per item : ', r['unit'])
                print('Quantity : ', r['quantity'])
                print('Total : ', r['cost'])
                print('\n')
        print('-----------------------------------------------')
        print('Total Purchase cost for the month : ', count)
        print('-----------------------------------------------')
def profit_report():

        print('Enter Month : ')
        month = input()
        print('Enter Year : ')
        year = input()
        count1=0.0
        count2=0.0
        with open('sales.csv','r+') as csvfile :
                reader = csv.DictReader(csvfile)
                for r in reader:
                        if r['sale_month']==month and r['sale_year']==year :
                                count1=count1+float(r['total'])
        with open('purchase.csv', 'r+') as csvfile :
                reader = csv.DictReader(csvfile)
                for r in reader:
                        if r['pur_month']==month and r['pur_year']==year :
                                count2=count2+float(r['cost'])
        profit = count1-count2
        print("Profit for ", month, " - ", year, " is ", profit, "!\n")


