#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// For medicines
void medicine_menu();
void add_medicine();
void search_medicine();
void medicine_to_be_purchased();
void update_inventory();

// For customer 
void customer_menu();
void search_customer();
void create_customer();
void update_customer_info();

// For supplier
void supplier_menu();
void search_supplier();
void create_supplier();
void update_supplier_info();

//For billing
void invoicing_menu();

//For reports
void report_menu();
void day_sale();
void month_sale();
void day_purchase();
void month_purchase();
void profit_report();

int main(void){
int menu_choice;
do{
	printf("Enter 1 for medicine menu. \n Enter 2 for customer menu. \n Enter 3 for supplier menu. \n Enter 4 for report menu. \n Enter 5 for Invoicing. \n Enter 6 to quit program.\n");
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

	case 6: printf("Exit Successful \n");
	break;

	default: printf("Invalid Input! Try Again! \n");

}

}while(menu_choice!= 6);

}

void medicine_menu(){
int medicine_menu_choice;
do{
	printf("Enter 1 to search medicine. \nEnter 2 to add medicine. \nEnter 3 to update inventory . \nEnter 4 for Medicines to be purchased list. \nEnter 5 to to go back to Main Menu.\n");
	scanf("%d",&medicine_menu_choice);

switch(medicine_menu_choice)
{
	case 1: search_medicine();
	break;

	case 2: add_medicine();
	break;

	case 3: update_inventory();
	break;

	case 4: medicine_to_be_purchased();
	break;

	case 5: printf("Returning to main menu \n");
	break;

	default: printf("Invalid Input! Try Again! \n");

}
}while(medicine_menu_choice!= 5);
}

void customer_menu(){
int customer_menu_choice;
do{
printf("Enter 1 to search customer. \nEnter 2 to create new customer. \nEnter 3 to update customer information. \nEnter 4 to go back to Main Menu.\n");
scanf("%d",&customer_menu_choice);

switch(customer_menu_choice)
{
	case 1: search_customer();
	break;

	case 2: create_customer();
	break;

	case 3: update_customer_info();
	break;

	case 4: printf("Returning to main menu!");
	break;

	default: printf("Invalid Input! Try Again! \n");
	
}

}while(customer_menu_choice!= 4);

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

	case 4: printf("Returning to main menu \n");
	break;

	default: printf("Invalid Input! Try Again! \n");

}

}while(supplier_menu_choice!= 4);

}

void report_menu(){
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

	case 6: printf("Returning to main menu \n");
	break;

	default: printf("Invalid Input! Try Again! \n");

}

}while(report_menu_choice != 6);

}

void invoicing_menu(){
	
}

