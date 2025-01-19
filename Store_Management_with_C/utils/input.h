#ifndef INPUT_H
#define INPUT_H

int saisie_int(int lb, int ub, char* msg, const char* color, const char* bold, const char* underline);

float saisie_float(float lb, float ub, char* msg, const char* color, const char* bold, const char* underline);

void saisie(char* p, char* msg, char lb, char ub, const char* color, const char* bold, const char* underline);

void saisie_v2(char* p, char* msg, const char* color, const char* bold, const char* underline);

void saisie_email(char* p, char* msg, const char* color, const char* bold, const char* underline);

int oui_ou_non(char* msg, const char* color, const char* bold, const char* underline);

#endif