#include<stdio.h>
#include<math.h>

int main()
{
    int a, b, c, n;
    for(a=1; a<500; a++)
    {
        for(b=1; b<500; b++)
        {
            for(c=1; c<500; c++)
            {
                if(a+b+c==1000 && a*a + b*b==c*c)
                {
                    n=a*b*c;
                    break;
                }
            }
        }
    }
    printf("%d", n);

    return 0;

}
