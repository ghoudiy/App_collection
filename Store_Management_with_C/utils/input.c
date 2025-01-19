#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "verif.h"
#include "display.h"

int saisie_int(int lb, int ub, char* msg, const char* color, const char* bold, const char* underline)
{
  int n;
  do
  {
    colored_text(msg, color, bold, underline);
    scanf("%d", &n);
  } while (n < lb || n > ub);
  return n;
}

float saisie_float(float lb, float ub, char* msg, const char* color, const char* bold, const char* underline)
{
  float n;
  do
  {
    colored_text(msg, color, bold, underline);
    scanf("%f", &n);
  } while (n < lb || n > ub);
  return n;
}

void saisie(char* p, char* msg, char lb, char ub, const char* color, const char* bold, const char* underline)
{
  do
  {
    colored_text(msg, color, bold, underline);
    scanf("%s", p);
  } while (!verif(p, lb, ub) || strlen(p) == 0);
}

void saisie_v2(char* p, char* msg, const char* color, const char* bold, const char* underline)
{
  do
  {
    colored_text(msg, color, bold, underline);
    scanf("%s", p);
  } while (!verif_v2(p, 'a', 'z', '0', '9', '_') || strlen(p) == 0);
}

void saisie_email(char* p, char* msg, const char* color, const char* bold, const char* underline)
{
  char* at, * pt;
  do
  {
    colored_text(msg, color, bold, underline);
    scanf("%s", p);
    at = strstr(p, "@");
    pt = strrchr(p, '.');
  } while (pt == NULL || at == NULL || !verif_email(p, at, pt));
}

int oui_ou_non(char* msg, const char* color, const char* bold, const char* underline)
{
  char yn;
  do
  {
    colored_text(msg, color, bold, underline);
    scanf(" %c", &yn);
  } while (tolower(yn) != 'o' && tolower(yn) != 'n');
  if (yn == 'o')
  {
    return 1;
  }
  else
  {
    return 0;
  }
}