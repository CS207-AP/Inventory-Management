import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()
date= d.strftime("%d")
month= d.strftime("%m")
year = d.strftime("%Y")
def sup_invoice():
	medi_name = input("Enter medicine name : ")
	med_id = input("Enter ID : ")
	unit = float(input("Enter cost price : "))
	quantity = int(input("Enter quantity : "))
	sup_id = input("Enter supplier id : ")
	cost = quantity * unit

	with open('purchase.csv','a+') as csvfile:
		columns = ['medi_name','med_id','unit','quantity','pur_date', 'pur_month','pur_year', 'sup_id','cost']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':date,'pur_month':month,'pur_year':year,'sup_id':sup_id,'cost':cost})
	
	tempfile = NamedTemporaryFile(mode='w', delete=False)
	with open('medicine.csv','r') as csvfile,tempfile:
		
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_pur']	
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(tempfile, fieldnames=columns)
		writer.writeheader()
		
		for row in reader:
			if row['medi_name'] == medi_name:
				row['quantity'] = int(row['quantity']) + quantity
				if int(row['quantity'])<int(row['min_quantity']):
					row['to_pur'] = int(row['min_quantity']) -int(row['quantity'])
				else:
					row['to_pur'] = 0	
			row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
			'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_pur':row['to_pur']}
			writer.writerow(row)
	shutil.move(tempfile.name, 'medicine.csv') 


def cust_invoice():
	i = 0
	medicinename = []
	medicnecost = []
	medicinequantity = []
	while i!=1:

		medi_name = input("Enter medicine name : ")
		med_id = input("Enter ID : ")
		sale = float(input("Enter sale price : "))
		quantity = int(input("Enter quantity : "))
		customer_name = input("Enter name of customer : ")
		customer_id = input("Enter customer id : ")
		total = quantity * sale
		medicinename.append(medi_name)
		medicnecost.append(sale)
		medicinequantity.append(quantity)
		
		
		tempfile = NamedTemporaryFile(mode='w', delete=False)

		with open('medicine.csv','r+') as csvfile,tempfile:

			columns = ['medi_name','med_id','sale','unit','quantity','min_quantity','comp_name','sup_id','to_pur']	
			reader = csv.DictReader(csvfile)
			writer = csv.DictWriter(tempfile, fieldnames=columns)
			writer.writeheader()

			for row in reader:
				if row['medi_name'] == medi_name:
					if quantity <=int(row['quantity']):
						row['quantity'] = int(row['quantity']) - quantity
					else:
						print("Only",int(row['quantity']),"remaining in stock")	
						break
					if int(row['quantity'])<int(row['min_quantity']):
						row['to_pur'] = int(row['min_quantity']) -int(row['quantity'])
					else:
						row['to_pur'] = 0
				row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
				'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_pur':row['to_pur']}
				writer.writerow(row)
		shutil.move(tempfile.name, 'medicine.csv') 

		with open('sales.csv','a+') as csvfile:
			columns = ['medi_name','med_id','sale','quantity','sale_date','sale_month','sale_year','customer_name', 'customer_id','total']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			
			writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'quantity':quantity,'sale_date':date,'sale_month':month,'sale_year':year,'customer_name':customer_name,'customer_id':customer_id,'total':total})
		
		print("Enter 0 for purchasing another medicine\nEnter 1 to print bill\n")
		i = int(input())
	
	print("|======Generating invoice======|\n")
	print("Ashoka Pharmacy\n")
	print("Date:", d.strftime("%x"),"\n")
	print("Time:", d.strftime("%X"),"\n")
	print("|Name======quantity=price=total|")
	for x in range(len(medicinename)):
		print("|",medicinename[x],"|",medicinequantity[x],"|",medicnecost[x],"|", medicinequantity[x] * medicnecost[x])
	print("|==============================|")
	print("|Grand Total===================|")
	grantotal =0
	for x in range(len(medicinename)):
		grantotal += medicinequantity[x] * medicnecost[x]
	print("Rs.",grantotal)
	print("|==========Thank You!==========|")







