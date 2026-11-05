#include<stdio.h>

 
int distinct(int a[], int n){
    
    int cnt = 1;
    // for (int i = 0; i < n; i++)
    // {
    //     int flag = 1;
    //     for (int j = i + 1; j < n; j++)
    //     {
    //         if(a[i] == a[j]){
    //             flag = 0;
    //             break;
    //         }
    //     }
    //     if(flag == 1){
    //         cnt ++;
    //     }
    // } 
    for (int i = 0; i < n-1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if(a[i] > a[j]){
                int tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
        }
    }
    int flag = 1;
     for (int j = 0; j < n-1; j++)
        {
            if(a[j] != a[j+1]){
                cnt++;
            }
        }
      
    return cnt;
}

int main()
{
    int n;
    scanf("%d",&n);
    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&a[i]);
    }
    
   int result =  distinct (a, n);
   printf("%d", result);
    return 0;
}