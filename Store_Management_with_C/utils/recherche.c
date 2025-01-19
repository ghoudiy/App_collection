#include <stdio.h>
#include <string.h>
#include "declaration.h"

// Client
int recherche_tel_client(client* arr_cl, int n, char* tel)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_cl[i].tel, tel);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

int recherche_email_client(client* arr_cl, int n, char* email)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_cl[i].email, email);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

void recherche_nom_client(client* arr_cl, int n, char* nom, client* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_cl[i].nom, nom) == 0)
    {
      arr[*narr] = arr_cl[i];
      (*narr)++;
    }
  }
}

void recherche_prenom_client(client* arr_cl, int n, char* prenom, client* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_cl[i].prenom, prenom) == 0)
    {
      arr[*narr] = arr_cl[i];
      (*narr)++;
    }
  }
}

// Fournisseur
int recherche_tel_fournisseur(fournisseur* arr_fo, int n, char* tel)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_fo[i].tel, tel);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

int recherche_email_fournisseur(fournisseur* arr_fo, int n, char* email)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_fo[i].email, email);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

void recherche_nom_fournisseur(fournisseur* arr_fo, int n, char* nom, fournisseur* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_fo[i].nom, nom) == 0)
    {
      arr[*narr] = arr_fo[i];
      (*narr)++;
    }
  }
}

void recherche_prenom_fournisseur(fournisseur* arr_fo, int n, char* prenom, fournisseur* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_fo[i].prenom, prenom) == 0)
    {
      arr[*narr] = arr_fo[i];
      (*narr)++;
    }
  }
}

int recherche_societe_fournisseur(fournisseur* arr_fo, int n, char* societe)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_fo[i].societe, societe);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

// Produit
int recherche_produit(produit* arr_pr, int n, char* id)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_pr[i].id, id);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

void recherche_descrp_produit(produit* arr_pr, int n, char* descrp, produit* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_pr[i].descrp, descrp) == 0)
    {
      arr[*narr] = arr_pr[i];
      (*narr)++;
    }
  }
}

int recherche_marque_produit(produit* arr_pr, int n, char* marque)
{
  short i = -1, test;
  do
  {
    i++;
    test = strcmp(arr_pr[i].marque, marque);
  } while (test != 0 && i < n - 1);
  return (test == 0) ? i : -1;
}

// Commande
void recherche_client_comnd(commande_client* arr_comnd, int n, char* tel, commande_client* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_comnd[i].tel, tel) == 0)
    {
      arr[*narr] = arr_comnd[i];
      (*narr)++;
    }
  }
}

void recherche_fournisseur_comnd(commande_client* arr_comnd, int n, char* marque, commande_client* arr, int* narr)
{
  *narr = 0;
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_comnd[i].marque, marque) == 0)
    {
      arr[*narr] = arr_comnd[i];
      (*narr)++;
    }
  }
}
