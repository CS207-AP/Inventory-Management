#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct supplier{
    int supplier_id;
    char supplier_name[30];
    char supplier_city[30];
    char supplier_contact[13];
    char supplier_email[40];
};

void search_supplier(){
    

}
void create_supplier(){
    struct supplier temp;
    FILE *fp=fopen("supplier.txt", "a+");
    printf("Enter the ID for the new supplier! \n");
    scanf("%d", &temp.supplier_id);
    printf("Enter the name of the supplier! \n");
    scanf("%s", &temp.supplier_name);
    printf("Enter the city of the supplier! \n");
    scanf("%s", &temp.supplier_city);
    printf("Enter the contact number of the supplier! \n");
    scanf("%d", &temp.supplier_contact);
    printf("Enter the email id of the supplier! \n");
    scanf("%s", &temp.supplier_email);
    fprintf(fp, "%d \n %s\n %s\n %d\n %s\n", temp.supplier_id, temp.supplier_name, temp.supplier_city, temp.supplier_contact, temp.supplier_email);
    fclose(fp);
    return;
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