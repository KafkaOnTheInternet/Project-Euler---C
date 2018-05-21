#include <stdio.h>
int main()
{
    long t1 = 1, t2 = 2;
    long nextTerm, sum=0;

    nextTerm = t1 + t2;

    while(nextTerm <= 4000000)
    {
        printf("%ld, ",nextTerm);
        if(nextTerm%2==0)
        {
            sum = sum + nextTerm;
        }

        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;

    }
    printf("\n %ld", sum);

    return 0;
}
