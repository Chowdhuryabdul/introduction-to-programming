#include<stdio.h>
#include<string.h>
int main()
{
    char s[10000001];
    scanf("%s", &s);
    int len = strlen(s);
    int sum = 0;
    for (int i = 0; i != len; i++)
    {
    //    sum += s[i] - 48;
       sum += s[i] - '0';
    // printf("%d \n", s[i]);
    }
    printf("%d", sum);    
}
