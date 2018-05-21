#include<stdio.h>

long triangleSum(long n)
{
    int sum=(n*(n+1))/2;
    return sum;
}
long checkDivisors(long n)
{
    long exponent=1, count=0, i;
    for(i=2; i<=n; i++, count=0)
    {
        if(n%i==0)
        {
            while(n%i==0)
            {
                n=n/i;
                count++;
            }
        }
        exponent=exponent*(count+1);
    }
    return exponent;
}

int main()
{
    long reqCount=500, triNum=1, reqSum;
    while(1)
    {
        reqSum=triangleSum(triNum);
        if(checkDivisors(reqSum)<=reqCount)
        {
            triNum++;
        }
        else
            break;
    }
    printf("%ld", triangleSum(triNum));

}
