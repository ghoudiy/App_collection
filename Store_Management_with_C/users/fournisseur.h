#ifndef FOURNISSEUR_H
#define FOURNISSEUR_H

#include "../utils/declaration.h"

int inscription_fournisseur(char* ffo, char* fpr);

void consulter_compte_fournisseur(fournisseur fo, char* fcomnd_gest);

void validation_commandes_fournisseur(fournisseur fo, char* fmag, char* fcomnd_gest, char* fpr);

#endif