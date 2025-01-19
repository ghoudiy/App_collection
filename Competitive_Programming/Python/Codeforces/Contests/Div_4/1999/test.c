#include<stdio.h>

int score(int a, int b) {
  if (a > b)
    return 1;
  if (a < b) 
    return -1;
  return 0;
}

void main() {
  int t, a1, a2, b1, b2, s = 0;
  scanf("%d", &t);
  while (t--) {
    s = 0;
    scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
    if (score(a1, b1) + score(a2, b2) > 0)
      s+= 2;
    if (score(a1, b2) + score(a2, b1) > 0)
      s+= 2;
    printf("%d\n", s);
  }
}  