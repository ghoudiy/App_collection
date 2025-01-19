#ifndef COMMON_H
#define COMMON_H

#include <time.h>
#include "declaration.h"

void chargerTabClient(char* file_name, client* array_client, int* n);
void chargerTabFournisseur(char* file_name, fournisseur* array_fournisseur, int* n);
void chargerTabProduit(char* file_name, produit* array_produit, int* n);
void chargerTabCommandeCl(char* file_name, commande_client* array_commande, int* n);
void chargerTabCommandeGest(char* file_name, commande_gest* array_commande, int* n);

void remplirFichClient(char* file_name, client* arr_cl, int n);
void remplirFichFournisseur(char* file_name, fournisseur* arr_fo, int n);
void remplirFichProduit(char* file_name, produit* arr_pr, int n);

int ajouter_client(char* fcl);
void ajouter_produit(produit* pr, char* fpr, char* marque);
int ajouter_fournisseur(char* ffo, char* fpr);

int comparer_date(struct tm now, date d2);
int comparer_date_v2(date d1, date d2);

void mise_a_jour_donnee(char* fcomnd_gest, char* ffo, char* fpr);

void verifier_mdp(char* msg, char* mdp, char* correct_mdp, const char* color, const char* bold, const char* underline);

#endif