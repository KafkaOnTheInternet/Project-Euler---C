#include<stdio.h>

int main()
{
    int n=40, flag=0, i=3;
    if(n%2 ==0)
    {
        while(flag==0)
        {
            for(n=40;;n++)
            {
                for(i=3; i<20; i++)
                {
                    if(n%i==0)
                        flag=1;
                    else
                    {
                        flag=0;
                        break;
                    }
                }
               if(flag==1)
                    break;
               else
                continue;
            }
        }


    }
    printf("%d", n);
    return 0;
}
