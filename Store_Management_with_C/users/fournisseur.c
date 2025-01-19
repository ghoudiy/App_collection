#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include "../utils/declaration.h"
#include "../utils/display.h"
#include "../utils/input.h"
#include "../utils/common.h"
#include "../utils/recherche.h"

int inscription_fournisseur(char* ffo, char* fpr)
{
  if (ajouter_fournisseur(ffo, fpr) == 0)
  {
    colored_text("Votre inscription a été réussie !", green, bold, underlined);
    return 1;
  }
  else
  {
    colored_text("L'inscription a échoué. Veuillez réessayer.", bright_red, bold, "");
    return 0;
  }
}

void consulter_compte_fournisseur(fournisseur fo, char* fcomnd_gest)
{
  colored_text("Veuillez selectionner l'une des actions suivantes: ", bright_white, "", "");
  printf("\n1. Afficher les informations personnelles");
  printf("\n2. Afficher l'historique des produits demandes et achetes");
  int choix = saisie_int(1, 2, "\nEntrez votre choix (1-2): ", bright_blue, "", "");
  char** tab = malloc(100 * sizeof(char*));
  int length[8] = { 0 };
  switch (choix)
  {
  case 1:
    remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
    print_fournisseur(fo, tab, length, 8);
    print_table(tab, length, 2, 8);
    break;
  case 2:
    colored_text("Veuillez selectionner l'une des actions suivantes: ", bright_white, "", "");
    printf("\n1. Afficher les produits vendus");
    printf("\n2. Afficher les produits demandes");
    choix = saisie_int(1, 2, "\nEntrez votre choix (1-2): ", bright_blue, "", "");
    commande_gest comnd_gest;
    int p;
    FILE* file = fopen(fcomnd_gest, "rb");
    if (file == NULL) {
      colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
      exit(1);
    }

    time_t t = time(NULL);
    struct tm now = *localtime(&t);
    float prix_total = 0;
    char aux[30], aux2[10];
    remplir_table(tab, length, 3, 0, "Produit", "Quantite", "Prix de vente unitaire");

    int i = 0;
    while (fread(&comnd_gest, size_comnd_gest, 1, file) == 1)
    {
      // printf("yassine: %s", comnd_gest.id);
      p = recherche_produit(fo.prod, fo.npr, comnd_gest.id);
      if (comparer_date(now, comnd_gest.dliv) == 1)
      {
        if (choix == 1)
        {
          i++;
          snprintf(aux2, 10, "%d", comnd_gest.qt);
          snprintf(aux, 30, "%f", fo.prod[p].pvu);
          remplir_table(tab, length, 3, i * 3, comnd_gest.id, aux2, aux);
          prix_total += fo.prod[p].pvu * comnd_gest.qt + fo.prod[p].tva;
        }
      }
      else if (choix == 2)
      {
        i++;
        snprintf(aux2, 10, "%d", comnd_gest.qt);
        snprintf(aux, 30, "%f", fo.prod[p].pvu);
        remplir_table(tab, length, 3, i * 3, comnd_gest.id, aux2, aux);
        prix_total += fo.prod[p].pvu * comnd_gest.qt + fo.prod[p].tva;
      }
    }
    print_table(tab, length, i + 1, 3);
    printf("Prix total: %f\n", prix_total);
  }
}

void validation_commandes_fournisseur(fournisseur fo, char* fmag, char* fcomnd_gest, char* fpr)
{

  magasin mag;
  FILE* file = fopen(fmag, "rb");
  fread(&mag, size_mag, 1, file);
  fclose(file);

  commande_gest comnd[100];
  int p, ncg, npr;
  produit arrpr[200], pr;
  chargerTabCommandeGest(fcomnd_gest, comnd, &ncg);
  chargerTabProduit(fpr, arrpr, &npr);
  short test;
  for (int i = 0; i < ncg; i++)
  {
    if (strcmp(fo.tel, comnd[i].tel_fo) == 0 && comnd[i].validee == 0) {
      test = 1;
      printf("Le magasin du numero %s a demnadee %u unites produit d'id %s\n", mag.tel, comnd[i].qt, comnd[i].id);
      if (oui_ou_non("Validez la commande? [O/n] ", bright_magenta, bold, "") == 1) {
        comnd[i].validee = 1;
        time_t t = time(NULL);
        time_t future_time = t + 3600 * 24 * 2;
        struct tm two_days_later = *localtime(&future_time);

        comnd[i].dliv.jj = two_days_later.tm_mday;
        comnd[i].dliv.mm = two_days_later.tm_mon + 1;
        comnd[i].dliv.an = two_days_later.tm_year + 1900;

        p = recherche_produit(arrpr, npr, comnd[i].id);
        int p2 = recherche_produit(fo.prod, fo.npr, comnd[i].id);

        pr = fo.prod[p2]; // Copy de produit
        pr.en_arrivage = 1;

        if (pr.qt < comnd[i].qt) {
          colored_text("La quantite demandee excede la quantite disponible en stock\n", bright_magenta, bold, "");
          colored_text("Veuillez selectionner l'une des actions suivantes: \n", bright_white, "", "");
          printf("1. Ajuster le prix d'achat unitaire\n2. Diminuer la quantite demandee");
          int choix = saisie_int(1, 2, "\nEntrez votre choix (1-2): ", bright_blue, "", "");
          switch (choix) {
          case 1:
            pr.pau = saisie_float(0.1, 10000, "Donner la nouveau prix d'achat unitaire: ", bright_white, "", "");
            break;
          case 2:
            pr.qt_en_att = saisie_int(1, 1000, "Donner la nouveau quantite: ", bright_white, "", "");
            break;
          }
        }
        else {
          pr.qt_en_att = comnd[i].qt;
        }

        if (p == -1) {
          pr.qt = 0;
          arrpr[npr++] = pr;
        }
        else {
          pr.qt = arrpr[p].qt;
          arrpr[p] = pr;
        }
      }
    }
  }

  if (test) {
    file = fopen(fpr, "wb");
    fwrite(arrpr, size_prod, npr, file);
    fclose(file);

    file = fopen(fcomnd_gest, "wb");
    fwrite(comnd, size_comnd_gest, ncg, file);
    fclose(file);
    printf("Commande valide aves succee");
  }
  else {
    printf("Aucun commande pour le moment\n");
  }
}
