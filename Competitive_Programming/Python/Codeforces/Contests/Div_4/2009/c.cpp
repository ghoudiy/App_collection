#include <iostream>
#include <math.h>
using namespace std;

int main()
{
  int t;
  long long int x, y, k, xf, yf;
  cin >> t;
  while (t--)
  {
    cin >> x >> y >> k;
    xf = x / k;
    yf = y / k;
    cout << max(xf, yf) * 2 + ((xf * k < x || yf * k < y) ? 2 : 0) << "\n";
  }
}