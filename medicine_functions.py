import csv
import sys
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()
def add_medicine():
	with open('medicine.csv','a+') as csvfile:
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'comp_name', 'sup_id','to_pur']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		
		medi_name = input("Enter medicine name : ")
		with open('medicine.csv','r+') as csfile:
			reader=csv.DictReader(csfile)
			for row in reader:
				if row['medi_name'] == medi_name:
					print("Medicine Already exists.")
					return

		med_id = input("Enter ID : ")
		sale = float(input("Enter sale price : "))
		unit = float(input("Enter cost price : "))
		quantity = int(input("Enter quantity : "))
		min_quantity = int(input("Enter min quantity to maintain : "))
		comp_name = input("Enter company name : ")
		sup_id = input("Enter supplier ID : ")
		cost = unit * quantity
		to_pur = min_quantity - quantity
		if quantity >min_quantity:
			to_pur = 0
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'unit':unit,'quantity':quantity,\
		'min_quantity':min_quantity,'comp_name':comp_name,'sup_id':sup_id,'to_pur':to_pur})

		
		with open('purchase.csv','a+') as csvfile:
			pur_date= d.strftime("%d")
			pur_month= d.strftime("%m")
			pur_year = d.strftime("%Y")
			columns = ['medi_name','med_id','unit','quantity','pur_date', 'pur_month','pur_year','sup_id','cost']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			
			writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':pur_date,'pur_month':pur_month,'pur_year':pur_year,'sup_id':sup_id,'cost':cost})


def search_medicine():
    with open('medicine.csv','r') as csvfile:
        name=input('Enter the medicine to search : ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'] == name:
                print(' Name :', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Price : ',row['sale'])	

def update_medicine():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['medi_name','med_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_pur']
    with open('medicine.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        med_name =input('Enter the name of the medicine you want to modify : ')
        for row in reader:
            if row['medi_name'] == med_name:
            	print('---------------------------------------------')
            	print('|1.To update Name                           |')
            	print('---------------------------------------------')
            	print('|2.To update Cost price                     |')
            	print('---------------------------------------------')
            	print('|3.To update Sale price                     |')
            	print('---------------------------------------------')
            	print('|4.To update supplier ID                    |')
            	print('---------------------------------------------')
            	choice=int(input())
            	if(choice==1):
            		row['medi_name']=input("Enter the new name : ")

            	elif(choice==2):
            		row['cost']=input("Enter the new cost price : ")

            	elif(choice==3):
            		row['sale']=input("Enter the new sale price : ")

            	elif(choice==4):
            		row['sup_id']=input("Enter the new supplier ID : ")    
            row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
		    'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_pur':row['to_pur']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'medicine.csv')
def medicine_to_be_purchased():
	count = 0
	with open('medicine.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if int(row['to_pur']) >0:
				count+=1
				print(' Name : ', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Minimum Quantity : ',row['min_quantity']\
				,'\n','To be purchased : ',row['to_pur'],'\n','Supplier ID : ',row['sup_id'])   
	if count == 0:
		print("No medicine to be purchased.\n")			        