#include <bits/stdc++.h>

using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  array<int, 5> arr[5];
  short min_swap = 0, pos_1;

  for (int i = 0; i < 5; i++) {
  
    for (int j = 0; j < 5; j++) {
      cin >> arr[i][j];
    }
  
    array<int, 5>::iterator start = arr[i].begin();
    pos_1 = (short)distance(start, find(start, start + 5, 1));
  
    if (pos_1 < 5) {
      min_swap = short(abs(pos_1 - 2) + abs(i - 2));
    }
  }

  cout << min_swap;

  return 0;
}