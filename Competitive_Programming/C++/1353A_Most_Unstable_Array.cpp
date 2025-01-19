#include <iostream>

using namespace std;

void solve() {
  long long int n, m;
  cin >> n >> m;
  if (n == 1) {
    cout << 0 << "\n";
  } else if (n > 2) {
    cout << m * 2 << "\n";
  } else {
    cout << m << "\n";
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