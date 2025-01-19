#include <stdio.h>
#include <math.h>

long long int max(long long int a, long long int b) {
    return (a > b) ? a : b;
}

int main()
{
  int t;
  long long int x, y, k, xf, yf;
  scanf("%d", &t);
  while (t--)
  {
    scanf("%lld%lld%lld", &x, &y, &k);
    xf = x / k;
    yf = y / k;
    printf("%lld\n", max(xf, yf) * 2 + ((xf * k < x || yf * k < y) ? 2 : 0));
  }
}
