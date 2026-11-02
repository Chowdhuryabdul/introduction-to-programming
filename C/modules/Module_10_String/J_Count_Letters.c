#include<stdio.h>
#include<string.h>
int main()
{
    char s[1000000];
    scanf("%s", &s);
    
    int len = strlen(s);
   int freq_arr[len];
//    for (int i = 0; i < len; i++)
//    {
//     freq_arr[i] = 0;
//    }

//    int cnta = 0, cntb = 0, cntc = 0;
//    int cnt = 0;
   for (int i = 0; i < len; i++)
   {
    // int dgt = s[i] - 48;
    // cnt = cnt + dgt;
    // freq_arr[dgt]++;
    freq_arr[s[i]]++;
}
// printf("%d", cnt);

  
   for (int i = 0; i < len; i++)
   {
    printf("%c : %d\n", s[i], freq_arr[i]);
    // printf("%d\n", freq_arr[i]);
   }


   
    

    return 0;
}