#include<stdio.h>
#include<string.h>
int main()
{
   int t; scanf("%d", &t);
   while (t--)
   {
    char s[100001];
   scanf("%s", &s);
   int len = strlen(s);
   int cnt_small = 0, cnt_cap = 0, cnt_dgt = 0;
   
   for ( int i = 0; i < len; i++)
   {
    
    if(s[i] >= 'a' && s[i] <= 'z'){
        cnt_small++;
    }else if(s[i] >= 'A' && s[i] <= 'Z'){
         cnt_cap++;
    }else if(s[i] >= '0' && s[i] <= '9'){
        cnt_dgt ++;
    }

   }
   printf("%d %d %d", cnt_cap, cnt_small, cnt_dgt);
   printf("\n");
   }
   
    return 0;
}