#include<stdio.h>
int main()
{
    int a;
    int b;
    scanf("%d %d", &a, &b);
    // printf("%d %d", a, b);
    int keep_value_of_a = a;
     a = b;
     b = keep_value_of_a;
    printf(" value of a: %d  value of b: %d ", a, b);
}