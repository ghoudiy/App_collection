#ifndef FOURNISSEUR_GEST_H
#define FOURNISSEUR_GEST_H

#include "../../utils/declaration.h"

void ajouter_fournisseur_gest(char* ffo, char* fpr);
int rechercher_fournisseur_gest(char* msg, short change, fournisseur* arrf, int* narrf, fournisseur* foc, int ub, char* ffo);
int pos_fournisseur(fournisseur* arr_fo, int n, char* msg, char* ffo);
void modifier_fournisseur_gest(char* ffo);
void supprimer_fournisseur_gest(char* ffo);
void afficher_fournisseur_gest(char* ffo);

#endif