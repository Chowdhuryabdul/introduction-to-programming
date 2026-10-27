#include<stdio.h>
// #include<string.h>
int main()
{
    // gets or fgets to take input with space
    // we will use fgets
    char s[50];
    // gets(s);
    fgets(s, 17, stdin);
    printf("%s", s);

}