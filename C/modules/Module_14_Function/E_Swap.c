#include<stdio.h>
void swap(int x, int y){
    int tmp = x;
    x = y;
    y = tmp;

    printf("%d %d", x, y);
}
int main()
{
    int x, y;
    scanf("%d %d", &x, &y);
     swap(x, y);
    return 0;
}