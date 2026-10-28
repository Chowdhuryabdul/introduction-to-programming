#include<stdio.h>
#include<string.h>
int main(){
    char a[200], b[200];
    scanf("%s %s", &a, &b);
    // int len = strlen(b);
    // int len_a = strlen(a);
    // for (int i = 0; i <= len; i++)
    // {
    //     a[len_a + i] = b[i];
    // }

    // function to strin concat
    strcat(a, b);
    printf("%s %s", a, b);
}