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
    printf("1. To add a new customer\n2. To view details of existing customer\n");
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
        }
    }
}