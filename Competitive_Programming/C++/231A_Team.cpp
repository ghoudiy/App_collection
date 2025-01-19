#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unsigned short int n, nrp = 0;
  cin >> n;
  while (n--) {
    int ar[3];
    cin >> ar[0] >> ar[1] >> ar[2];
    if (count(begin(ar), end(ar), 1) >= 2) {
      nrp++;
    }
  }
  cout << nrp;
  return 0;
}