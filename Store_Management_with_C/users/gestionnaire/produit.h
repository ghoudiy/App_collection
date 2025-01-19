#ifndef PRODUIT_GEST_H
#define PRODUIT_GEST_H

#include "../../utils/declaration.h"

int ajouter_produit_gest(char* fpr);
int rechercher_produit_gest(char* msg, short change, produit* array_prod, int* narrpr, produit* pro, int ub, char* fpr);
void modifier_produit_gest(char* fpr);
void supprimer_produit_gest(char* fpr);
void afficher_produit_gest(char* fpr);

#endif