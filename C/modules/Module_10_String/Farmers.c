#include<stdio.h>
#include<string.h>
int main()
{
  int t;
  scanf("%d", &t);
  while (t--)
  {
       int m1, m2, d;
   scanf("%d %d %d", &m1, &m2, &d);
   int total_farmer = m1 + m2;
   int total_days_needed = d * m1 / total_farmer;
   int fewer_day = d - total_days_needed;
   printf("%d\n", fewer_day);
  }

    return 0;
}