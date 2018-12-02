#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct supplier{
    int supplier_id;
    char supplier_name[30];
    char supplier_city[20];
    int supplier_contact;
    char supplier_email[50];
};
void sup_search_byid(){
    printf("Enter the supplier ID to find details!\n");
    int temp_id;
    struct supplier temp;
    scanf("%d", &temp_id);
    FILE *f=fopen("supplier.txt", "a+");
    rewind(f);
    while(fscanf(f,"%d \n %s\n %s\n %d\n %s\n", &temp.supplier_id, temp.supplier_name, temp.supplier_city, &temp.supplier_contact, temp.supplier_email)!=EOF){
        if(temp_id==temp.supplier_id){
            printf("Supplier Found!\n");
            printf("Supplier id: %d\n", temp.supplier_id);
            printf("Supplier name: %s\n", temp.supplier_name);
            printf("Supplier city: %s\n", temp.supplier_city);
            printf("Supplier contact: %d\n", temp.supplier_contact);
            printf("Supplier email: %s\n", temp.supplier_email);
        }
        else{
            printf("Supplier does not exist!\n");
        }
    }
    fclose(f);
    return;
}
void sup_search_byname(){
    printf("Enter the supplier name to find details!\n");
    char *temp_name=malloc(sizeof(char*));
    struct supplier temp;
    scanf("%s", temp_name);
    FILE *f=fopen("supplier.txt", "a+");
    rewind(f);
    while(fscanf(f,"%d \n %s\n %s\n %d\n %s\n", &temp.supplier_id, temp.supplier_name, temp.supplier_city, &temp.supplier_contact, temp.supplier_email)!=EOF){
        if(strcmp(temp_name, temp.supplier_name)==0){
            printf("Supplier Found!\n");
            printf("Supplier id: %d\n", temp.supplier_id);
            printf("Supplier name: %s\n", temp.supplier_name);
            printf("Supplier city: %s\n", temp.supplier_city);
            printf("Supplier contact: %d\n", temp.supplier_contact);
            printf("Supplier email: %s\n", temp.supplier_email);
        }
    }
    fclose(f);
    return;
}
void search_supplier(){
    int sup_search_choice;
    do{
    printf("Enter 1 to search supplier by id!\nEnter 2 to search supplier by name!\nEnter 3 to Exit!\n");
    scanf("%d", &sup_search_choice);
    switch(sup_search_choice){
        case 1: sup_search_byid();
        break;
        case 2: sup_search_byname();
        break;
        case 3: printf("Exit Successful!\n");
        break;
        default:printf("Invalid Input!\n");
    }
    }while(sup_search_choice!=3);
}
void create_supplier(){
    struct supplier temp;
    FILE *fp=fopen("supplier.txt", "a+");
    printf("Enter the ID for the new supplier! \n");
    scanf("%d", &temp.supplier_id);
    printf("Enter the name of the supplier! \n");
    scanf("%s", temp.supplier_name);
    printf("Enter the city of the supplier! \n");
    scanf("%s", temp.supplier_city);
    printf("Enter the contact number of the supplier! \n");
    scanf("%d", &temp.supplier_contact);
    printf("Enter the email id of the supplier! \n");
    scanf("%s", temp.supplier_email);
    fprintf(fp, "%d \n %s\n %s\n %d\n %s\n", temp.supplier_id, temp.supplier_name, temp.supplier_city, temp.supplier_contact, temp.supplier_email);
    fclose(fp);
    return;
}
void update_supplier_info(){

}

int main(void){
int supplier_menu_choice;

do{
	printf("Enter 1 to search supplier. \nEnter 2 to create new supplier. \nEnter 3 to update supplier information. \nEnter 4 to go back to Main Menu.\n");
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