#include<stdio.h>>
int main()
{
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    int dx;
    scanf("%d", &dx);
    for (int i = dx; i < n-1; i++)
    {
        a[i] = a[i+1];
    }
    // n--; it means sixe of array is n - 1
     for (int i = 0; i < n-1; i++)
    {
        printf("%d ", a[i]);
    }
    
    
}