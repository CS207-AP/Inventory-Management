import csv
def add_medicine():
	with open('medicine.csv','a+') as csvfile:
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date','pur_date','comp_name', 'supp_name','cost','total']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		writer.writeheader()
		medi_name = input("Enter medicine name")
		med_id = input("Enter ID")
		sale = float(input("Enter sale price"))
		unit = float(input("Enter cost price"))
		quantity = int(input("Enter quantity"))
		min_quantity = int(input("Enter min quantity to maintain"))
		exp_date = input("Enter exp date")
		pur_date= input("Enter purchase date")
		comp_name = input("Enter company name")
		supp_name = input("Enter supplier name")
		cost = quantity * unit
		total = quantity *sale
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'unit':unit,'quantity':quantity,'min_quantity':min_quantity, 'exp_date':exp_date,'pur_date':pur_date,'comp_name':comp_name, 'supp_name':supp_name,'cost':cost,'total':total})

