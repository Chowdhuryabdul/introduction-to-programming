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
    int m;
    scanf("%d", &m);
    int b[m];
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &b[i]);
    }
    
    int new_array[n+m];
    for (int i = 0; i < n+m; i++)
    {
        new_array[i] = a[i];
        
    }
    for (int i = 0; i < m; i++)
    {
        new_array[i + n] = b[i];
    }
   
    for (int i = 0; i < n+m; i++)
    {
        printf("%d ", new_array[i]);
    }
    
}