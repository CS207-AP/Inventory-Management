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
	total = quantity * unit

	with open('purchase.csv','a+') as csvfile:
		columns = ['medi_name','med_id','unit','quantity','pur_date','sup_name', 'sup_id','total']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':pur_date,'sup_name':sup_name,'sup_id':sup_id,'total':total})
	tempfile = NamedTemporaryFile(mode='w', delete=False)
	
	with open('medicine.csv','r') as csvfile,tempfile:
		
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date',\
		'pur_date','comp_name', 'supp_id','cost','total','to_pur']	
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(tempfile, fieldnames=columns)
		writer.writeheader()
		
		for row in reader:
			if row['medi_name'] == medi_name:
				row['quantity'] = int(row['quantity']) + quantity
			row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
			'min_quantity':row['min_quantity'],'exp_date':row['exp_date'],'pur_date':row['pur_date'],'comp_name':row['comp_name'], \
			'supp_id':row['supp_id'],'cost':row['cost'],'total':row['total'],'to_pur':row['to_pur']}
			writer.writerow(row)
	shutil.move(tempfile.name, 'medicine.csv') 
def cust_invoice():
	print("TEST")