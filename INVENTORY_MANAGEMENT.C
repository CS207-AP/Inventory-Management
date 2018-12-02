#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void medicine_menu();
void customer_menu();
void supplier_menu();
void report_menu();
void invoicing_menu();

void main(){
int menu_choice;
do{
printf("Enter 1 for medicine menu. \n Enter 2 for customer menu. \n Enter 3 for supplier menu. \n Enter 4 for report menu. \n Enter 5 for Invoicing. \n Enter 6 to quit program.");
scanf("%d",&menu_choice);

switch(menu_choice)
{
	case 1: medicine_menu();
	break;

	case 2: customer_menu();
	break;

	case 3: supplier_menu();
	break;

	case 4: report_menu();
	break;

	case 5: invoicing_menu();
	break;

	default: break;

}

}while(m != 6);

}

void medicine_menu(){
int machine_menu_choice;
do{
printf("Enter 1 to search medicine. \nEnter 2 to add medicine. \nEnter 3 to update inventory . \nEnter 4 for Medicines to be purchased list. \nEnter 5 to to go back to Main Menu.");
scanf("%d",&machine_menu_choice);

switch(machine_menu_choice)
{
	case 1: search_medicine();
	break;

	case 2: add_medicine();
	break;

	case 3: update_inventory();
	break;

	case 4: medicine_to_be_purchased();
	break;

	default: break;
}

}while(m != 5);

}

void customer_menu(){
int customer_menu_choice;
do{
printf("Enter 1 to search customer. \nEnter 2 to create new customer. \nEnter 3 to update customer information. \nEnter 4 to go back to Main Menu.");
scanf("%d",&machine_menu_choice);

switch(machine_menu_choice)
{
	case 1: search_customer();
	break;

	case 2: create_customer();
	break;

	case 3: update_customer_info();
	break;

	default: break;
}

}while(m != 5);

}

void supplier_menu(){
int supplier_menu_choice;
do{
printf("Enter 1 to search supplier. \nEnter 2 to create new supplier. \nEnter 3 to update supplier information. \nEnter 4 to go back to Main Menu.");
scanf("%d",&supplier_menu_choice);

switch(supplier_menu_choice)
{
	case 1: search_supplier();
	break;

	case 2: create_supplier();
	break;

	case 3: update_supplier_info();
	break;

	default: break;
}

}while(m != 4);

}

void main(){
int report_menu_choice;
do{
printf("Enter 1 for Todays sales. \n Enter 2 for this months sales. \n Enter 3 for todays purchases. \n Enter 4 for this months purchases. \n Enter 5 for profit report. \n Enter 6 to go back to main menu.");
scanf("%d",&report_menu_choice);

switch(report_menu_choice)
{
	case 1: day_sale();
	break;

	case 2: month_sale();
	break;

	case 3: day_purchase();
	break;

	case 4: month_purchase();
	break;

	case 5: profit_report();
	break;

	default: break;

}

}while(m != 6);

}

void invoicing_menu();{
	
}

