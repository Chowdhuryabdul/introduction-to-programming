#include<stdio.h>
#include<string.h>
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
       char s[101];
    scanf("%s", &s);
    int str_len = strlen(s);
    int cnt = 0;
    int i = 0;
    for (int i = 0; i < str_len; i++)
    {
        cnt ++;
    }

   if(cnt > 10)
   {
    printf("%c%d%c", s[i], str_len - 2, s[str_len - 1]);
   }
   else
   {
    printf("%s", s);
   }
   printf("\n");
    }
    

    
    

}