#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  short n, k, nrp = 0;
  cin >> n >> k;
  vector<int> ar(n);

  for (short i = 0; i < n; i++) {
    cin >> ar.at(i);
  }

  if (ar.at(0) == 0) {
    cout << 0;
  } else {
    for (short i = 0; i < n; i++) {
      if (ar.at(i) >= ar.at(k - 1) && ar.at(i) > 0) {
        nrp++;
      }
    }
    cout << nrp;
  }

  return 0;
}