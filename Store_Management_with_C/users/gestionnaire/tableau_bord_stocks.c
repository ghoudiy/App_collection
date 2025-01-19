#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include "../../utils/recherche.h"
#include "../../utils/display.h"
#include "../../utils/common.h"
#include "../../utils/declaration.h"

void afficher_prod_dispo(char* fpr)
{
  FILE* file = fopen(fpr, "rb");
  produit pr;
  char** tab = malloc(100 * sizeof(char*));
  int length[7] = { 0 }, ntab = 1;
  remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
  while (fread(&pr, size_prod, 1, file) == 1)
  {
    if (pr.qt > 0 && pr.en_arrivage == 0)
    {
      print_produit(pr, tab, length, ntab * 7, 0);
      ntab++;
    }
  }
  print_table(tab, length, ntab, 7);
}

void afficher_prod_en_att(char* fpr)
{
  FILE* file = fopen(fpr, "rb");
  produit pr;
  char** tab = malloc(100 * sizeof(char*));
  int length[7] = { 0 }, ntab = 1;
  remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
  while (fread(&pr, size_prod, 1, file) == 1)
  {
    if (pr.en_arrivage == 1)
    {
      printf("EN attent: %d\n", pr.qt_en_att);
      print_produit(pr, tab, length, ntab * 7, 1);
      ntab++;
    }
  }
  print_table(tab, length, ntab, 7);
}

void consulter_cl_prod(char* fcl, char* fcomnd_cl)
{
  commande_client arr[100], arr_comnd[100], arr_comnd_en_att[100];
  client cl;
  int n = 0, nc, narr;

  time_t t = time(NULL);
  struct tm now = *localtime(&t);

  chargerTabCommandeCl(fcomnd_cl, arr_comnd, &nc);
  FILE* file = fopen(fcl, "rb");
  char tel[10] = { '0' };
  printf("Les client qu'ont achetes des produits: \n");
  while (fread(&cl, size_cl, 1, file) == 1)
  {
    recherche_client_comnd(arr_comnd, nc, cl.tel, arr, &narr);
    if (narr > 0)
    {
      for (int i = 0; i < narr; i++)
      {
        if (comparer_date(now, arr[i].dliv) == 1)
        {
          if (strcmp(arr[i].tel, tel) != 0) {
            printf("Prenom: %s, Nom: %s, Tel: %s\n", arr[i].prenom, arr[i].nom, arr[i].tel);
            printf("Les produits achetes: \n------------------------------\n");
            strcpy(tel, arr[i].tel);
          }
          printf("Produit: %s, Description: %s, Marque: %s, Quantite: %u, Date d'achat: %u/%u/%u\n", arr[i].id, arr[i].descrp, arr[i].marque, arr[i].qt, arr[i].dach.an, arr[i].dach.mm, arr[i].dach.jj);
        }
        else
        {
          arr_comnd_en_att[n++] = arr[i];
        }
      }
    }
  }
  printf("------------------------------\n");
  printf("Les clients ayant acheté des produits mais en attente de livraison\n");
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_comnd_en_att[i].tel, tel) != 0)
    {
      printf("Prenom: %s, Nom: %s, Tel: %s\n", arr_comnd_en_att[i].prenom, arr_comnd_en_att[i].nom, arr_comnd_en_att[i].tel);
      printf("Les produits commandes: \n------------------------------\n");
      strcpy(tel, arr_comnd_en_att[i].tel);
    }
    printf("Produit: %s, Description: %s, Marque: %s, Quantite: %u, Date d'achat: %u/%u/%u\n", arr_comnd_en_att[i].id, arr_comnd_en_att[i].descrp, arr_comnd_en_att[i].marque, arr_comnd_en_att[i].qt, arr_comnd_en_att[i].dach.an, arr_comnd_en_att[i].dach.mm, arr_comnd_en_att[i].dach.jj);
  }
  printf("------------------------------\n");
}

void consulter_fournisseur_prod(char* ffo, char* fcomnd_cl)
{
  commande_client arr[100], arr_comnd[100], arr_comnd_en_att[100];
  fournisseur fo;
  int n = 0, nc, narr;

  time_t t = time(NULL);
  struct tm now = *localtime(&t);

  FILE* file = fopen(ffo, "rb");
  chargerTabCommandeCl(fcomnd_cl, arr_comnd, &nc);

  char marque[20] = "";

  printf("La liste des fournisseurs avec les produits vendus: \n");
  while (fread(&fo, size_fo, 1, file) == 1)
  {
    recherche_fournisseur_comnd(arr_comnd, nc, fo.societe, arr, &narr);
    if (narr > 0)
    {
      for (int i = 0; i < narr; i++)
      {
        if (comparer_date(now, arr[i].dliv) == 1)
        {
          if (strcmp(arr[i].marque, marque) != 0)
          {
            printf("\nSociete: %s\n", arr[i].marque);
            printf("Les produits vendus: \n");
            strcpy(marque, arr[i].marque);
          }
          printf("Produit: %s, Description: %s, Quantite: %u, Date d'achat: %u/%u/%u\n", arr[i].id, arr[i].descrp, arr[i].qt, arr[i].dach.an, arr[i].dach.mm, arr[i].dach.jj);
        }
        else
        {
          arr_comnd_en_att[n++] = arr[i];
        }
      }
    }
  }

  printf("La liste des fournisseurs avec les produits en attente: \n");
  for (int i = 0; i < n; i++)
  {
    if (strcmp(arr_comnd_en_att[i].marque, marque) != 0)
    {
      printf("\nSociete: %s\n", arr_comnd_en_att[i].marque);
      printf("Les produits commandes:\n");
      strcpy(marque, arr_comnd_en_att[i].marque);
    }
    printf("Produit: %s, Description: %s, Quantite: %u, Date d'achat: %u/%u/%u\n", arr_comnd_en_att[i].id, arr_comnd_en_att[i].descrp, arr_comnd_en_att[i].qt, arr_comnd_en_att[i].dach.an, arr_comnd_en_att[i].dach.mm, arr_comnd_en_att[i].dach.jj);
  }
}
