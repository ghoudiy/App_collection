#ifndef VERIF_H
#define VERIF_H

#include "declaration.h"

int verif(char *p, char lb, char ub);
int verif_v2(char *p, char lb, char ub, char lb2, char ub2, char x);
int verif_email(char *p, char *at, char *pt);

#endif