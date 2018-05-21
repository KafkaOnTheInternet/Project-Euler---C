#include<stdio.h>

unsigned long sequence(unsigned long n)
{
    int count=0;
    while(n!=1)
    {
        if(n%2==0)
            n=n/2;
        else
            n=(3*n)+1;
        count++;
    }
    return count;
}


int main()
{
    unsigned long i, max=0, number=0;
    max=sequence(1);
    for(i=1; i<1000000; i+=2)
    {
        if(sequence(i)>max)
        {
            max=sequence(i);
            number=i;

        }

    }
   printf("%lu", number);
}
