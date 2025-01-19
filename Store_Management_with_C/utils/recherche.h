#ifndef RECHERCHE_H
#define RECHERCHE_H

#include "declaration.h"
// Client
int recherche_tel_client(client* arr_cl, int n, char* tel);
int recherche_email_client(client* arr_cl, int n, char* email);
void recherche_nom_client(client* arr_cl, int n, char* nom, client* arr, int* narr);
void recherche_prenom_client(client* arr_cl, int n, char* prenom, client* arr, int* narr);

// Fournisseur
int recherche_tel_fournisseur(fournisseur* arr_fo, int n, char* tel);
int recherche_email_fournisseur(fournisseur* arr_fo, int n, char* email);
void recherche_nom_fournisseur(fournisseur* arr_fo, int n, char* nom, fournisseur* arr, int* narr);
void recherche_prenom_fournisseur(fournisseur* arr_fo, int n, char* prenom, fournisseur* arr, int* narr);
int recherche_societe_fournisseur(fournisseur* arr_fo, int n, char* societe);

// Produit
int recherche_produit(produit* arr_pr, int n, char* id);
int recherche_marque_produit(produit* arr_pr, int n, char* marque);
void recherche_descrp_produit(produit* arr_pr, int n, char* descrp, produit* arr, int* narr);

// Commande
void recherche_client_comnd(commande_client* arr_comnd, int n, char* tel, commande_client* arr, int* narr);
void recherche_fournisseur_comnd(commande_client* arr_comnd, int n, char* marque, commande_client* arr, int* narr);
#endif