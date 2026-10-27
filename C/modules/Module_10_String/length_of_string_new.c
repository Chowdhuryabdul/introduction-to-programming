#include<stdio.h>
#include<string.h>
int main()
{
    char s[30];
    scanf("%s", &s);
    // printf("%s", s);
    int cnt = 0;

    // for (int i = 0; s[i] != '\0'; i++)
    // {
    //     cnt ++;
    // }

    int sze = strlen(s);
    printf("%d",sze)    ;
}
