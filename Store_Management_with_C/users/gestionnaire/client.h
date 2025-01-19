#ifndef CLIENT_GEST_H
#define CLIENT_GEST_H

#include "../../utils/declaration.h"

void ajouter_client_gest(char* fcl);

int rechercher_client_gest(char* msg, short change, client* arrc, int* narrc, client* clc, int ub, char* fcl);

int pos_client(client* arr_cl, int n, char* msg, char* fcl);

void modifier_client_gest(char* fcl);

void supprimer_client_gest(char* fcl);

void afficher_client_gest(char* fcl);

#endif