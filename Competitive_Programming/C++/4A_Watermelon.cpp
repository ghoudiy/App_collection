#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unsigned short int w;
  cin >> w;

  cout << ((w > 2 && w % 2 == 0) ? "YES" : "NO");

  return 0;
}