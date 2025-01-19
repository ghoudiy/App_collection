#ifndef CLIENT_H
#define CLIENT_H

#include "../utils/declaration.h"

int inscription_client(char* fcl);

void acheter_produit_client(client cl, char* fpr, char* fcomnd_cl, char* fnoti);

void demande_facture_client(client cl, char* fcomnd_cl, char* fmag);

void consulter_compte_client(client cl, char* fcomnd_cl, char* fmag);

#endif