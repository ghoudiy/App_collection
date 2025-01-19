#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  short n, sum = 0;
  
  cin >> n;
  string st;
  for (int i = 0; i < n; i++) {
    cin >> st;
    if (st.find("+") != st.npos) {
      sum++;
    } else {
      sum--;
    }
  }
  cout << sum;

  return 0;
}