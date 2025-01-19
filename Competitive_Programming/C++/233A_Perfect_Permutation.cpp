#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  if (n == 1 || n % 2 == 1) {
    cout << -1;
  } else {
    string nums;
    for (int i = 1; i <= n; i += 2) {
      nums.append((to_string(i + 1) + " " + to_string(i) + " "));
    }
    cout << nums;
  }
  return 0;
}