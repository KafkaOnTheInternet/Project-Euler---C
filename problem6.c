#include<stdio.h>
#include<math.h>

int main()
{
    long long sum, a, b, c, n=100;
    a=(n*(n+1)*(2*n+1))/6;
    b=n*(n+1)/2;
    c=pow(b,2);
    sum=a-c;
    printf("%lld", sum);
}
