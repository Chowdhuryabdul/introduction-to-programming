#include<stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int space = n - 1;
    int star = 1;
    for (int i = 0; i < n; i++)
    {
         for (int i = 0; i < space; i++)
        {
           printf(" ");
            
        }
         for( int j = 0; j < star; j++)
            {
                printf("*");
            }
       
        printf("\n");
        star+=2;
        space--;
    }
    int space_1 = 0;
    int star_1 = 2*n-1;
    for (int i = 0; i < n; i++)
    {
         for (int i = 0; i < space_1; i++)
        {
           printf(" ");
            
        }
         for( int j = 0; j < star_1; j++)
            {
                printf("*");
            }
       
        printf("\n");
        star_1-=2;
        space_1++;
    }
     printf("\n");
    return 0;
}