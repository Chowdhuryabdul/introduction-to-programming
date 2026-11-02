#include<stdio.h>
#include<string.h>
int main()
{
   char s[100001];
   scanf("%s", &s);
   int len = strlen(s);
   int con = 0;
   for ( int i = 0; i < len; i++)
   {
    if(s[i] != 'a' && s[i] != 'e' && s[i] != 'o' && s[i] != 'i' && s[i] != 'u' ){
        con ++;
    }
   }
   printf("%d", con);
   
    return 0;
}