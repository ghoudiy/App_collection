#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string a, b;
  cin >> a >> b;

  short i = -1, len = (short)a.length();
  bool test = true;
  while (++i < len && test) {
    test = tolower(a[i]) == tolower(b[i]);
  }

  if (test) {
    cout << 0;
  } else if (tolower(a[i - 1]) > tolower(b[i - 1])) {
    cout << 1;
  } else {
    cout << -1;
  }

  return 0;
}