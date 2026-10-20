#include<stdio.h>
int main()
{
    int A, I, P, E;
    scanf("%d %d %d %d", &A, &I, &P, &E);
//    printf("%d %d %d %d", A, I, P, E);

if(A >= 21 && A <= 35){
    if(I >= 80 && I <= 100){
        if(P >= 70 && P <= 100){
            if(E >= 2){
                printf("Selected");
            }else if(E < 2){
                if(A >= 30 && I >= 95 && P >= 90 ){
                    printf("Selected");
                }else{
                    printf("Rejected");
                }
            }
            else{
                 printf("Rejected");
            }
        }
        else{
             printf("Rejected");
        }
    }
    else{
        printf("Rejected");
    }
}
else{
    printf("Rejected");
}

    
}