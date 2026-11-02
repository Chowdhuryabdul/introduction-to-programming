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
    int a1[m];
 
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &a1[i]);
    }
    
    int new[n+m];
    for (int i = 0; i < n; i++)
    {
        new[i] = a[i];
    }
    for (int i = 0; i < m; i++)
    {
        new[i+n] = a1[i];
    }
    
    for (int i = 0; i < n+m; i++)
    {
        printf("%d ", new[i]);
    }
    
  
    
    
    return 0;
}