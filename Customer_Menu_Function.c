#include<stdio.h>

struct cusmen
{
    char name[50];
    int id;
    long phone;
    char med[50];
};

void cusmen();

int main()
{
    cusmen();
}

void cusmen()
{
    char ch='y';
    do
    {
    printf("1. To add a new customer\n2. To view details of existing customer\n3. To update an existing record\n");
    int c;
    scanf("%d",&c);
    switch(c)
    {
        case 1:
        {
        struct cusmen a;
        printf("---------------------Customer Details------------------------\n");
        FILE *fp=fopen("cusmen.txt","a+");
        printf("Enter the name of the customer\n");
        scanf("%s",&a.name);
        printf("Enter the ID of the customer\n");
        scanf("%d",&a.id);
        printf("Enter the phone number of the customer\n");
        scanf("%ld",&a.phone);
        printf("Enter the name of the drug the customer needs\n");
        scanf("%s",&a.med);
        fprintf(fp,"%s \n%d \n%ld \n %s\n",a.name,a.id,a.phone,a.med);
        fclose(fp);
        break;
        }
        case 2:
        {
            printf("Enter the customer ID to find details\n");
            int n;
            struct cusmen b;
            scanf("%d",&n);
            FILE *fp1=fopen("cusmen.txt","a+");
            rewind(fp1);
            while(fscanf(fp1,"%s %d %ld %s",&b.name,&b.id,&b.phone,&b.med)!=EOF)
                {
                    if(n==b.id)
                    printf("Customer Name:%s\n Customer ID: %d\n Customer Phone: %ld\n Customer Medicine: %s\n",b.name,b.id,b.phone,b.med);
                }
            
            fclose(fp1);
            break;
        }
        case 3:
        {
            printf("Enter the customer ID to update that particular record\n");
            int n1;
            struct cusmen c;
            scanf("%d",&n1);
            FILE *fp2=fopen("cusmen.txt","a+");
            FILE *fp2_1=fopen("temp.txt","a+");
            rewind(fp2);
            while(fscanf(fp2,"%s %d %ld %s",&c.name,&c.id,&c.phone,&c.med)!=EOF)
            {
                if(n1!=c.id)
                fprintf(fp2_1,"%s \n%d \n%ld \n %s\n",c.name,c.id,c.phone,c.med);
                else
                {
                    printf("1. To update customer name\n2. To update customer ID\n3. To update customer phone number\n4. To update customer medicine\n");
                    int choice;
                    scanf("%d",&choice);
                    switch(choice)
                    {
                        case 1:
                        {
                            printf("Enter the name\n");
                            scanf("%s",&c.name);
                            break;
                        }
                        case 2:
                        {
                            printf("Enter the ID\n");
                            scanf("%d",&c.id);
                            break;
                        }
                        case 3:
                        {
                            printf("Enter the phone number\n");
                            scanf("%ld",&c.phone);
                            break;
                        }
                        case 4:
                        {
                            printf("Enter the medicine name\n");
                            scanf("%s",&c.med);
                            break;
                        }
                    }
                    fprintf(fp2_1,"%s \n%d \n%ld \n %s\n",c.name,c.id,c.phone,c.med);
                
                }
                fclose(fp2_1);
                fclose(fp2);
                fp2=fopen("cusmen.txt","w");
                fp2_1=fopen("temp.txt","r");
                while(fscanf(fp2_1,"%s %d %ld %s",&c.name,&c.id,&c.phone,&c.med)!=EOF)
                fprintf(fp2,"%s \n%d \n%ld \n %s\n",c.name,c.id,c.phone,c.med);
                fclose(fp2);
                fclose(fp2_1);
            }
          
        }
        printf("Do you want to go again(y/n)?");
        scanf("%c",&ch);
    }
<<<<<<< HEAD:CusMen.c
  }while(ch=='Y' || ch=='y');
}
=======
}
>>>>>>> 5a82015c330405c43d4beb1aae785155053e189a:Customer_Menu_Function.c
