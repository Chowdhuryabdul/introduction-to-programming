#include<stdio.h>
#include<string.h>
#include<stdbool.h>

int main()
{
    char a[200], b[200];
    scanf("%s %s", &a, &b);

    // this is manual way
    int i = 0;
    // while (true)
    // {
    //     if(a[i] == '\0' && b[i] == '\0'){
    //         printf("Equal");
    //         break;
    //     }else if(a[i] == '\0'){
    //         printf("A is smaller");
    //         break;
    //     }else if(b[i] == '\0'){
    //         printf("B is smaller");
    //         break;
    //     }else if(a[i] < b[i]){
    //         printf("A is smaller");
    //         break;
    //     }else if(a[i] > b[i]){
    //         printf("B is smaller");
    //         break;
    //     }else if(a[i] == b[i]){
    //         i++;
    //     }
    // }

    // we can do it with function
//    printf("%d",strcmp(a, b) ) ;
    // it return an integer value
    // if first string is smalle than it returns -1. in compiler it can give -4 or any negative integer
    // if second string is smalle than it return 1
    // if both are equal it will return 0
  
    // we can write it like this
    int val = strcmp(a, b);
    if(val < 0){
        printf("A is smaller");
    }else if ( val > 0){
        printf("B is smaller");
    }else if (val == 0){
        printf("Equal");
    }

    
}
