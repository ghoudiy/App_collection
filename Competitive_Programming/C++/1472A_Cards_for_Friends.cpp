#include <bits/stdc++.h>

using namespace std;

int div_2(int num) {
  int s = 1;
  while (num % 2 == 0) {
    s *= 2;
    num = num / 2;
  }
  return s;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  short t, w, h;
  long long int n;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> w >> h >> n;
    if (n > 1) {
      int aux = div_2(w) * div_2(h);
      cout << ((aux >= n) ? "YES\n" : "NO\n");
    } else {
      cout << "YES\n";
    }
  }
  return 0;
}