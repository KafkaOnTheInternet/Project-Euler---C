#include<stdio.h>

int main()
{
    unsigned long long x=0;
    for(int i=0; i<1000; i++)
    {
        if(i%3==0 || i%5==0)
            x+=i;
    }
    printf("%llu", x);
}
