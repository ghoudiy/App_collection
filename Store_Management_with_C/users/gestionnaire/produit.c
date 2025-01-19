#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utils/recherche.h"
#include "../../utils/input.h"
#include "../../utils/common.h"
#include "../../utils/display.h"
#include "../../utils/declaration.h"

int ajouter_produit_gest(char* fpr)
{
  produit pr;
  ajouter_produit(&pr, fpr, "");

  FILE* file = fopen(fpr, "ab");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
    return 1;
  }
  fwrite(&pr, size_prod, 1, file);
  fclose(file);
  colored_text("\nLe produit a ete ajoute avec success !\n", bright_green, "", "");
  return 0;
}

int rechercher_produit_gest(char* msg, short change, produit* array_prod, int* narrpr, produit* pro, int ub, char* fpr)
{
  int narr, n;
  produit arr_pr[100], arr[100];
  char id[20], descrp[50], marque[40];
  chargerTabProduit(fpr, arr_pr, &n);

  if (strlen(msg) > 0)
  {
    printf("%s", msg);
  }
  else
  {
    colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche :", bright_blue, "", "");
    printf("\n1. Description\n2. Marque\n3. ID");
  }

  int choix, p;
  ub += 3 * (!ub);
  char message[30];
  snprintf(message, 30, "\nEntrez votre choix (1-%d): ", ub);
  choix = saisie_int(1, ub, message, bright_yellow, "", "");
  switch (choix)
  {

  case 1:
    saisie_v2(descrp, "Donner la description du produit a chercher: ", white, "", "");
    recherche_descrp_produit(arr_pr, n, descrp, arr, &narr);
    if (narr > 0)
    {
      afficher_list_produit(arr, narr);
      if (change)
      {
        memcpy(array_prod, arr, sizeof(arr));
        *narrpr = narr;
      }
      return 1;
    }
    else
      colored_text("La description est incorrect ou le produit n'est existe pas\n", bright_red, "", "");
    break;

  case 2:
    saisie_v2(marque, "Donner la marque du produit a chercher: ", white, "", "");
    if ((p = recherche_marque_produit(arr_pr, n, marque)) != -1)
    {
      char** tab = malloc(20 * sizeof(char*));
      int length[7] = { 0 };
      remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
      print_produit(arr_pr[p], tab, length, 7, 0);
      print_table(tab, length, 2, 7);
      if (change)
        *pro = arr_pr[p];
      return 1;
    }
    else
      colored_text("La marque est incorrect ou le produit n'est existe pas\n", bright_red, "", "");
    break;

  case 3:
    saisie_v2(id, "Donner l'id du produit a chercher: ", white, "", "");
    if ((p = recherche_produit(arr_pr, n, id)) != -1)
    {
      char** tab = malloc(20 * sizeof(char*));
      int length[7] = { 0 };
      remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
      print_produit(arr_pr[p], tab, length, 7, 0);
      print_table(tab, length, 2, 7);
      if (change)
        *pro = arr_pr[p];
      return 1;
    }
    else
      colored_text("L'id est incorrect ou le produit n'est existe pas\n", bright_red, "", "");
    break;
  }
  return 0;
}

int pos_produit(produit* arr_pr, int n, char* msg, char* fpr)
{
  int p;
  char id[20], aux[100];
  strcpy(aux, msg);
  strcat(aux, "(Taper 0 si tu oublies l'id): ");
  saisie_v2(id, aux, white, "", "");
  if (strcmp(id, "0") == 0)
  {
    do
    {
      colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche", bright_blue, "", "");
    } while (rechercher_produit_gest("\n1. Description\n2. Marque", 0, NULL, NULL, NULL, 2, fpr) == 0);
    saisie_v2(id, msg, white, "", "");
  }
  do {
    p = recherche_produit(arr_pr, n, id);
    if (p == -1) {
      colored_text("Ce id est introuvable\n", bright_red, "", "");
      saisie_v2(id, msg, white, "", "");
    }

  } while (p == -1);
  return p;
}

void modifier_produit_gest(char* fpr)
{
  char id[20];
  int choix;
  produit arr_pr[100];
  int n = 0, p;
  chargerTabProduit(fpr, arr_pr, &n);
  p = pos_produit(arr_pr, n, "\nDonner l'id du produit a modifier: ", fpr);

  afficher_list_ordonee(produit_informations, 7);
  choix = saisie_int(1, 7, "Souhaitez-vous modifier le? ", bright_cyan, "", "");
  switch (choix)
  {
  case 1:
    do
    {
      saisie_v2(id, "Veuillez introduire le nouveau id: ", bright_white, "", "");
    } while (recherche_produit(arr_pr, n, id) != -1);
    strcpy(arr_pr[p].id, id);
    break;
  case 2:
    arr_pr[p].qt = saisie_int(0, 1000, "Veuillez introduire la nouveau quantite: ", bright_white, "", "");
    break;
  case 3:
    saisie_v2(arr_pr[p].descrp, "Veuillez introduire la nouveau description: ", bright_white, "", "");
    break;
  case 4:
    saisie_v2(arr_pr[p].marque, "Veuillez introduire la nouveau marque: ", bright_white, "", "");
    break;
  case 5:
    arr_pr[p].pau = saisie_float(0.1, 10000, "Veuillez introduire la nouveau prix d'achat uniaire: ", bright_white, "", "");
    break;
  case 6:
    arr_pr[p].pvu = saisie_float(0.1, 10000, "Veuillez introduire la nouveau prix de vente uniaire: ", bright_white, "", "");
    break;
  case 7:
    arr_pr[p].tva = saisie_float(0.1, 50, "Veuillez introduire le nouveau TVA: ", bright_white, "", "");
    break;
  }
  remplirFichProduit(fpr, arr_pr, n);
  colored_text("La modification se fait avec succee", bright_green, "", "");
}

void supprimer_produit_gest(char* fpr)
{
  produit arr_pr[100];
  int n = 0, p;
  chargerTabProduit(fpr, arr_pr, &n);

  p = pos_produit(arr_pr, n, "\nDonner l'id du produit a supprimer: ", fpr);
  FILE* file = fopen(fpr, "wb");
  for (int i = 0; i < n; i++)
  {
    if (i != p)
    {
      fwrite(&arr_pr[i], size_prod, 1, file);
    }
  }
  fclose(file);
}

void afficher_produit_gest(char* fpr)
{
  FILE* file = fopen(fpr, "rb");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
  }
  else
  {
    char** tab = malloc(100 * sizeof(char*));
    int length[7] = { 0 }, ntab = 1;
    remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
    produit pr;
    while (fread(&pr, size_prod, 1, file) == 1)
    {
      print_produit(pr, tab, length, ntab * 7, 0);
      ntab++;
    }
    print_table(tab, length, ntab, 7);
  }
  fclose(file);
}