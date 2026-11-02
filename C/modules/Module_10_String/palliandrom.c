#include<stdio.h>
int main()
{
     int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    int flag = 1;
    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        // printf("%d", a[i]);
        
            if(a[i] != a[j]){
                flag = 0;
                break;
            
        }
        
        
    }
    if(flag == 1){
        printf("yes");
    }else{
         printf("no");
    }
    
    
    return 0;
}