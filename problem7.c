#include<stdio.h>
#include<math.h>

int isPrime(int n)
{
    int j=0, flag=0;
    if(n%2==0)
        return 0;
    for(j=3; j*j<=n; j+=2)
    {
        if(n%j==0)
            return 0;
    }
        return 1;
}

int main()
{
    int count=0, i=1;

    while(count!=10001)
    {
        if(isPrime(i++))
            count++;

    }
    printf("%d", i-1);
    return 0;

}

/*#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
  int r, f;
  if(n==1)
    return 0;
  else if(n<4)
    return 1;
  else if(n%2==0)
    return 0;
  else if(n<9)
    return 1;
  else if(n%3==0)
    return 0;
  else
  {
    r=sqrt(n);
    f=5;
    while(f<=r)
    {
      if(n%f==0)
      {
        return 0;
      }
      if(n%(f+2)==0)
      {
        return 0;
      }
      f=f+6;
    }
  }
  return 1;
}

int main(void)
{
  int limit=10001, count=1, i=1;
  while(count!=limit)
  {
    if(isPrime(i))
    {
      i+=2;
      count++;
    }
    else
      i+=2;


  }
  printf("%d", i);

	return 0;
} */
