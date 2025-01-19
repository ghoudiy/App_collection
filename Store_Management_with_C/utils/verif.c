#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include "declaration.h"

int verif(char *p, char lb, char ub) {
  int test;
  do {
    test = tolower(*p) >= lb && tolower(*p) <= ub;
    p++;
  } while (test && *p != '\0');
  return test;
}

int verif_v2(char *p, char lb, char ub, char lb2, char ub2, char x) {
  int test;
  do {
    test = (tolower(*p) >= lb && tolower(*p) <= ub) || (tolower(*p) >= lb2 && tolower(*p) <= ub2) || *p == x;
    p++;
  } while (test && *p != '\0');
  return test;
}

int verif_email(char *p, char *at, char *pt) {
  char aux[20];
  strncpy(aux, p, strlen(p) - strlen(at));
  aux[strlen(p) - strlen(at)] = '\0';
  return strlen(pt) - strlen(at) > 0 && verif_v2(aux, 'a', 'z', '0', '9', '.');
}
