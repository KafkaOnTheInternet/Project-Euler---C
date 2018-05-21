#include<stdio.h>

int num_divisors(int n)
{
    int divisors=1, count=0, p=3;
    if(n%2==0)
    {
        n=n/2;
    }
    while(n%2==0)
    {
        count++;
        n=n/2;
    }
    divisors=divisors*(count+1);

    while(n!=1)
    {
        count=0;
        while(n%p==0)
        {
            count++;
            n=n/p;
        }
        divisors=divisors*(count+1);
        p+=2;
    }
    return divisors;
}
int find_triangular_index(int factor_limit)
{
    int n=1, temp;
    int lnum=num_divisors(n);
    int rnum=num_divisors(n+1);
    while(lnum*rnum<500)
    {
        n++;
        lnum=rnum;
        rnum=num_divisors(n+1);
    }

    return n;

}

int main()
{
    int index, triangle;
    index=find_triangular_index(500);
    triangle=(index*(index+1))/2;
    printf("%d", triangle);

}
