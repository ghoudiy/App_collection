#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unsigned short int n;
  cin >> n;
  string line;
  unsigned short int len;
  for (int i = 0; i < n; ++i) {
    cin >> line;
    len = (short)line.length();
    if (len > 10) {
      cout << line[0] << len - 2 << line[len-1] << "\n";
    } else {
      cout << line << "\n";
    }
  }

  return 0;
}