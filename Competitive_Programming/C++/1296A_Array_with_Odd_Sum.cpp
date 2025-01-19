#include <iostream>
#include <vector>

using namespace std;

void solve() {
  short n, odd = 0;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a.at(i);
    if (a.at(i) % 2 == 1) {
      odd++;
    }
  }
  if (odd == 0 || (odd == n && odd % 2 == 0)) {
    cout << "NO\n";
  } else {
    cout << "YES\n";
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  short t;
  cin >> t;
  while (t--) {
    solve();
  }

  return 0;
}