#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define MAX 2000000

int main()
{
    long long *a, i, p, sum=0, limit;
    limit=sqrt(MAX);
    a=malloc(sizeof(long long)* MAX);
    for(i=0; i<MAX; i++)
        a[i]=i+1;
    for(i=2; i<=MAX/2; i++)
    {
        if(a[i]!= -1)
        {
            for(p=2; i*p<=MAX; p++)
            {
                a[i*p-1]=-1;
            }
        }
    }
    for(i=0; i<MAX; i++)
    {
        if(a[i]!=-1)
            sum = sum + a[i];
    }

    printf("%lld", sum-1);

}
