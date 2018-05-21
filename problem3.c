#include<stdio.h>
#include<math.h>

int main()
{
    long long i, maxPrime, n=600851475143;
    for(i=3; i<sqrt(n); i+=2)
    {
        if(n%i==0)
        {
            maxPrime=i;
            n=n/i;
        }
    }
    printf("%lld %lld", maxPrime, n);
    return 0;
}
