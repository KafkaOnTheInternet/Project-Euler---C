#include<stdio.h>
int palindrome(int x)
{
    int original, new=0, max=0;
    original=x;
    while(x>0)
    {
        new= new*10 + x%10;
        x=x/10;
    }
    if(original==new)
        return original;
    else
        return 0;
}

int main()
{
    int a, b, c, max;
    for(a=999; a>=1; a--)
    {
        for(b=999; b>=1; b--)
        {
            c=palindrome(a*b);
            if(c!=0 && c>max)
            {

              max=c;
            }
        }
    }
    printf("%d", max);
    return 0;
}
