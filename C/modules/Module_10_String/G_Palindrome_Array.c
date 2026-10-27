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
       
        if(a[i] != a[j]){
            flag = 0;
        }
    }
    
    if(flag == 1)
    {
        printf("YES\n");
    }
    else{
        printf("NO\n");
    }
    // int new_array[n];
    // for (int i = 0; i < n; i++)
    // {
    //    new_array[i] = a[i];
    // }
    // int i = 0, j = n - 1;
    // while (i < j)
    // {
    //     int tmp = new_array[i];
    //     new_array[i] = new_array[j];
    //     new_array[j] = tmp;
    //     i++, j--;
    // }
    // for (int i = 0; i < n; i++)
    // {
    //    printf("%d ", new_array[i]);
    // }
    
    // if(a[i] == new_array[i]){
    //     printf("YES\n");
    // }else{
    //     printf("NO\n");
    // }
}