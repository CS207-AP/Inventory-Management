#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct medical
{
	char id[6];
	char medi_name[20];
	int quantity;
	float sale;
	float total;
	float unit;
	float cost;
	float profit;
	int qty;
	char pur_date[15];
	char exp_date[15];
	char manu_date[15];
	char comp_name[20];
	char supp_name[30];
 };

 struct medical *temp;




void main(){
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