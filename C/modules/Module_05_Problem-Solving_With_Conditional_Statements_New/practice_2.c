#include<stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int x;
    int win = 0;
    int mx_win = 0;

    for(int i = 1; i <= n; i++)
    {
        scanf("%d", &x);
        if(x == 1)
        {
           win++;
        }else{
            win = 0;
        }
      if(win > mx_win){
        mx_win = win;
      }
    } 
    printf("%d\n", mx_win);
}

