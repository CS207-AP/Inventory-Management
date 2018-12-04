#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct medicine
{
	char id[6];
	char medi_name[20];
	int quantity;
	float sale;
	float total;
	float unit;
	float cost;
	int min_quantity;
	char pur_date[15];
	char exp_date[15];
	char comp_name[20];
	char supp_name[30];
 };

 struct medicine *temp;


void add_medicine(){
	FILE *fm1;
	struct medicine medical;

	fm1 = fopen("medicine.txt", "a+");
	
        printf("Enter the name of the medicine\n");
        scanf("%s",medical.medi_name);
        printf("Enter the medicine ID\n");
        scanf("%s",medical.id);
        printf("Enter quantity purchased\n");
        scanf("%d",&medical.quantity);
        printf("Enter minimum quantity to be kept in stock\n");
        scanf("%d",&medical.min_quantity);
        printf("Enter sale price\n");
        scanf("%f",&medical.sale);
        printf("Enter cost price\n");
        scanf("%f",&medical.unit);
        printf("Enter company name\n");
        scanf("%s",medical.comp_name);
        printf("Enter supplier name\n");
        scanf("%s",medical.supp_name);
        printf("Enter Expiery date\n");
        scanf("%s",medical.exp_date);
        printf("Enter purchase date\n");
        scanf("%s",medical.pur_date);
        rewind(fm1);
        fwrite(&medical,sizeof(struct medicine),1,fm1);
        //fprintf(fm1,"%s %s %d %d %f %f %s %s %s %s \r\n",medical.medi_name,medical.id,medical.quantity,medical.min_quantity,medical.sale,medical.unit,medical.comp_name,medical.supp_name,medical.exp_date,medical.pur_date);
        fclose(fm1);

}

void search_medicine(){
	printf("Enter the name of the medicine\n");
            char med_name[20];
            struct medicine medical;
            scanf("%s",med_name);
            FILE *fm2=fopen("medicine.txt","r");
            rewind(fm2);
            while(fread(&medical,sizeof(struct medicine),1,fm2)==1)
                { 
                 fread(&medical,sizeof(struct medicine),1,fm2);
                 printf("here1");
                 printf("%s\n",medical.medi_name);
                    if(strcmp(medical.medi_name,med_name)==0){
                    	printf("here2");
                    printf("Medicine Name:%s\n Medicine quantity:%d\nMedicine company:%s\nMedicine Price:%f\n",medical.medi_name,medical.quantity,medical.comp_name,medical.sale);
                }}
            
            fclose(fm2);
}

void main(){
int medicine_menu_choice;
do{
printf("Enter 1 to search medicine. \nEnter 2 to add medicine. \nEnter 3 to update inventory . \nEnter 4 for Medicines to be purchased list. \nEnter 5 to to go back to Main Menu.");
scanf("%d",&medicine_menu_choice);

switch(medicine_menu_choice)
{
	case 1: search_medicine();
	break;

	case 2: add_medicine();
	break;
/*
	case 3: update_inventory();
	break;

	case 4: medicine_to_be_purchased();
	break;*/

	default: break;
}

}while(medicine_menu_choice != 5);

}