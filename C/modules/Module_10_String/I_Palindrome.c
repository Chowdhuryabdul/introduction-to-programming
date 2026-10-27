#include<stdio.h>
#include<string.h>
int main()
{
   
    char s[1001];
    scanf("%s", &s);
    int len = strlen(s);

    char s_new[1001];
    int i = 0;

     for (int i = 0; i < len; i++)
    {
         s_new[i] = s[i];
    }
     for (int i = 0, j = len - 1; i < j; i++, j--)
    {
      

        int tmp = s_new[i];
       s_new[i] = s_new[j];
       s_new[j] = tmp;

        
    }

    //  for (int i = 0; i < len; i++)
    // {
    //     printf("%c", s_new[i]);
    // }
    
    

    if(s[i] != s_new[i]){
        printf("NO\n");
    }else{
        printf("YES\n");
    }


    // int flag = 1;

    // for (int i = 0, j = len - 1; i < j; i++, j--)
    // {
    //     if(s[i] != s[j]){
    //         flag = 0;
    //         printf("NO");
    //         break;
    //     }
    // }
    
    // if(flag == 1){
    //     printf("YES\n");
    // }
    // else{
    //      printf("NO\n");
    // }

}