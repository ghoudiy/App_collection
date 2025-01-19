#include <iostream>
#include <vector>

using namespace std;

void solve()
{
  short n;
  cin >> n;
  vector<short> a(n);
  for (int i = 0; i < n; i++)
  {
    cin >> a.at(i);
  }
  short nro = 0;
  for (int i = 0; i < n; i++)
  {
    if (a.at(i) % 2 == 1)
    {
      nro++;
    }
  }
  cout << ((nro % 2 == 0) ? "YES\n" : "NO\n");
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);

  short t;
  cin >> t;
  while (t--)
  {
    solve();
  }

  return 0;
}