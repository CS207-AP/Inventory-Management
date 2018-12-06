import csv
from tempfile import NamedTemporaryFile
import shutil

def sup_invoice():
	medi_name = input("Enter medicine name:")
	med_id = input("Enter ID:")
	unit = float(input("Enter cost price"))
	quantity = int(input("Enter quantity"))
	pur_date = (input("Enter min quantity to "))
	sup_name = input("Enter name of supplier")
	sup_id = input("Enter supplier id")
	cost = quantity * unit

	with open('purchase.csv','a+') as csvfile:
		columns = ['medi_name','med_id','unit','quantity','pur_date','sup_name', 'sup_id','cost']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':pur_date,'sup_name':sup_name,'sup_id':sup_id,'cost':cost})
	tempfile = NamedTemporaryFile(mode='w', delete=False)

	with open('medicine.csv','r') as csvfile,tempfile:
		
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date',\
		'pur_date','comp_name', 'supp_id','to_pur']	
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(tempfile, fieldnames=columns)
		writer.writeheader()
		
		for row in reader:
			if row['medi_name'] == medi_name:
				row['quantity'] = int(row['quantity']) + quantity
			row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
			'min_quantity':row['min_quantity'],'exp_date':row['exp_date'],'pur_date':row['pur_date'],'comp_name':row['comp_name'], \
			'supp_id':row['supp_id'],'to_pur':row['to_pur']}
			writer.writerow(row)
	shutil.move(tempfile.name, 'medicine.csv') 


def cust_invoice():
	i = 0
	medicinename = []
	medicnecost = []
	medicinequantity = []
	while i!=1:

		medi_name = input("Enter medicine name:")
		med_id = input("Enter ID:")
		sale = float(input("Enter cost price"))
		quantity = int(input("Enter quantity"))
		sale_date = input("Enter min quantity to ")
		customer_name = input("Enter name of supplier")
		customer_id = input("Enter supplier id")
		total = quantity * unit
		medicinename.append(medi_name)
		medicnecost.append(sale)
		medicinequantity.append(quantity)
		with open('sales.csv','a+') as csvfile:
			columns = ['medi_name','med_id','unit','quantity','sale_date','customer_name', 'customer_id','sale']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			writer.writeheader()
			writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'quantity':quantity,'sale_date':sale_date,'customer_name':customer_name,'customer_id':customer_id,'total':total})
		
		tempfile = NamedTemporaryFile(mode='w', delete=False)

		with open('medicine.csv','r') as csvfile,tempfile:

			columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date',\
			'pur_date','comp_name', 'supp_id','to_pur']	
			reader = csv.DictReader(csvfile)
			writer = csv.DictWriter(tempfile, fieldnames=columns)
			writer.writeheader()

			for row in reader:
				if row['medi_name'] == medi_name:
					row['quantity'] = int(row['quantity']) - quantity
				row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
				'min_quantity':row['min_quantity'],'exp_date':row['exp_date'],'pur_date':row['pur_date'],'comp_name':row['comp_name'],\
				'supp_id':row['supp_id'],'to_pur':row['to_pur']}
				writer.writerow(row)
		shutil.move(tempfile.name, 'medicine.csv') 
		print("Enter 1 for purchasing another medicine\nEnter 0 to print bill")
		i = int(input())
	print("|=========Generating invoice==========|\n")
	print("Ashoka Pharmacy\n")
	print("Date:", sale_date,"\n")
	print("Time:", sale_date,"\n")
	print("|=====================================|\n")
	print("|Name=========quantity===price===total|")
	for x in range(len(medicinename)):
		print("|",medicinename[x],"|",medicinequantity[x],"|",medicnecost[x],"|", medicinequantity[x] * medicnecost[x])
	print("|=====================================|")
	print("|Grand Total==========================|")
	grantotal =0
	for x in range(len(medicinename)):
		grantotal += medicinequantity[x] * medicnecost[x]
	print("Rs.",grantotal)
	print("|==============Thank You!=============|")







