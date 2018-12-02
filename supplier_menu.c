#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct supplier{
    int supplier_id[10];
    char name[30];
    char city[30];
    char contact[13];
    char email[40];
};

void search_supplier(){

}
void create_supplier(){

}
void update_supplier_info(){

}

int main(void){
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