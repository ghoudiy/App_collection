#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include "gestionnaire/tableau_bord_stocks.h"
#include "../utils/common.h"
#include "../utils/display.h"
#include "../utils/recherche.h"
#include "../utils/input.h"
#include<unistd.h>
int inscription_client(char* fcl)
{
  if (ajouter_client(fcl) == 0)
  {
    colored_text("Votre inscription a été réussie !\n", green, bold, underlined);
    return 1;
  }
  else
  {
    colored_text("L'inscription a échoué. Veuillez réessayer.\n", bright_red, bold, "");
    return 0;
  }
}

void envoyer_noti_gest(char* id, unsigned qt_cl, unsigned stock, char* tel, char* fnoti)
{
  FILE* file = fopen(fnoti, "a");
  fprintf(file, "Le client portant le numero %s souhaite commander %u unites du produit avec l'ID %s, mais il ne reste que %u unites en stock\n", tel, qt_cl, id, stock);
  fclose(file);
}

void acheter_produit_client(client cl, char* fpr, char* fcomnd_cl, char* fnoti)
{
  produit arr_pr[100];
  commande_client comnd_cl;
  int npr, p;
  chargerTabProduit(fpr, arr_pr, &npr);
  afficher_prod_dispo(fpr);
  saisie_v2(comnd_cl.id, "Donner l'id du produit qui vous voulez l'acheter: ", white, "", "");
  p = recherche_produit(arr_pr, npr, comnd_cl.id);
  if (p == -1)
  {
    colored_text("L'id est incorrect ou le produit n'est existe pas", bright_red, "", "");
  }
  else if (arr_pr[p].qt == 0)
  {
    if (arr_pr[p].en_arrivage == 1) {
      colored_text("Le produit est en cours d'arrivage", bright_red, "", "");
    }
    else {
      colored_text("Le produit est hors stock", bright_red, "", "");
    }
  }
  else
  {
    do
    {
      comnd_cl.qt = saisie_int(1, 1000, "Donner la quantite du produit voulu: ", white, "", "");
      if (comnd_cl.qt > arr_pr[p].qt)
      {
        colored_text("La quantité que vous demandez n'est pas disponible. Elle dépasse le stock disponible\n", bright_red, "", "");
        envoyer_noti_gest(comnd_cl.id, comnd_cl.qt, arr_pr[p].qt, comnd_cl.tel, fnoti);
      }
    } while (comnd_cl.qt > arr_pr[p].qt);

    // Diminuer la quantite en stock
    arr_pr[p].qt -= comnd_cl.qt;

    strcpy(comnd_cl.tel, cl.tel);
    strcpy(comnd_cl.nom, cl.nom);
    strcpy(comnd_cl.prenom, cl.prenom);
    strcpy(comnd_cl.descrp, arr_pr[p].descrp);
    strcpy(comnd_cl.marque, arr_pr[p].marque);

    time_t t = time(NULL);
    struct tm now = *localtime(&t);
    comnd_cl.dach.jj = now.tm_mday;
    comnd_cl.dach.mm = now.tm_mon + 1;
    comnd_cl.dach.an = now.tm_year + 1900;

    time_t future_time = t + 3600 * 24 * 2;
    struct tm two_days_later = *localtime(&future_time);

    comnd_cl.dliv.jj = two_days_later.tm_mday;
    comnd_cl.dliv.mm = two_days_later.tm_mon + 1;
    comnd_cl.dliv.an = two_days_later.tm_year + 1900;
    comnd_cl.pau = arr_pr[p].pau;
    comnd_cl.tva = arr_pr[p].tva;

    FILE* file = fopen(fcomnd_cl, "ab");
    if (fwrite(&comnd_cl, size_comnd_cl, 1, file) != 1) {
      colored_text("Error writing data\n", bright_red, "", "");
      exit(1);
    }
    fclose(file);
    colored_text("L'achat a été effectué avec succès !\n", bright_green, bold, underlined);

    remplirFichProduit(fpr, arr_pr, npr);
  }
}

void demande_facture_client(client cl, char* fcomnd_cl, char* fmag)
{
  commande_client arr_cc[100], arr[100];
  int ncc, narr;
  chargerTabCommandeCl(fcomnd_cl, arr_cc, &ncc);
  recherche_client_comnd(arr_cc, ncc, cl.tel, arr, &narr);
  if (narr > 0)
  {
    short timb = print_magasin(fmag);
    char** tab = malloc(100 * sizeof(char*));
    char aux[15], aux2[10], aux3[30], aux4[30];
    int length[5] = { 0 };
    remplir_table(tab, length, 5, 0, "Produit", "Date d'achat", "Quantite", "Prix unitaire", "TVA");
    srand(time(NULL));
    printf("Numero de facture: %d, Nom: %s\n", rand(), cl.nom);
    float prix_total = 0;
    for (int i = 0; i < narr; i++)
    {
      snprintf(aux, 15, "%d/%d/%d", arr[i].dach.an, arr[i].dach.mm, arr[i].dach.jj);
      snprintf(aux2, 10, "%d", arr[i].qt);
      snprintf(aux3, 30, "%.3f", arr[i].pau);
      snprintf(aux4, 30, "%.3f", arr[i].tva);
      remplir_table(tab, length, 5, (i + 1) * 5, arr[i].id, aux, aux2, aux3, aux4);
      prix_total += arr[i].pau * arr[i].qt + arr[i].tva;
    }
    print_table(tab, length, narr + 1, 5);
    printf("Prix total: %f", timb + prix_total);
  }
}

void consulter_compte_client(client cl, char* fcomnd_cl, char* fmag)
{
  colored_text("Veuillez selectionner l'une des actions suivantes: ", bright_white, "", "");
  printf("\n1. Afficher les informations personnelles");
  printf("\n2. Afficher l'historique des produits demandes et achetes");
  int choix = saisie_int(1, 2, "\nEntrez votre choix (1-2): ", bright_blue, "", "");
  char** tab = malloc(150 * sizeof(char*));
  int length[9] = { 0 };
  switch (choix)
  {
  case 1:
    remplir_table(tab, length, 9, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe", "Date de naissance");
    print_client(cl, tab, length, 9);
    print_table(tab, length, 2, 9);
    break;
  case 2:

    magasin mag;
    FILE* file = fopen(fmag, "rb");
    fread(&mag, size_mag, 1, file);
    fclose(file);

    time_t t = time(NULL);
    struct tm now = *localtime(&t);

    commande_client comnd_cl;
    float prix_total = 0;
    file = fopen(fcomnd_cl, "rb");
    if (file == NULL) {
      colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
      exit(1);
    }
    char aux[30], aux2[10];
    int i = 0;
    remplir_table(tab, length, 5, 0, "ID Produit", "Quantite", "Description", "Marque", "Prix d'achat unitaire");

    colored_text("Veuillez selectionner l'une des actions suivantes: ", bright_white, "", "");
    printf("\n1. Afficher les produits achetes");
    printf("\n2. Afficher les produits en attents");

    choix = saisie_int(1, 2, "\nEntrez votre choix (1-2): ", bright_blue, "", "");
    while (fread(&comnd_cl, size_comnd_cl, 1, file) == 1)
    {
      // printf("comparer_date(now, comnd_cl.dliv) = %d", comparer_date(now, comnd_cl.dliv));
      // printf("now.tm_year = %d, d2.an = %d | now.tm_mon = %d, d2.mm = %d | now.tm_mday = %d, d2.jj = %d\n", now.tm_year, comnd_cl.dliv.an, now.tm_mon, comnd_cl.dliv.mm, now.tm_mday, comnd_cl.dliv.jj);
      if (strcmp(comnd_cl.tel, cl.tel) == 0)
      {
        if (comparer_date(now, comnd_cl.dliv) == 1)
        {
          if (choix == 1)
          {
            i++;
            snprintf(aux, 30, "%f", comnd_cl.pau);
            snprintf(aux2, 10, "%u", comnd_cl.qt);
            remplir_table(tab, length, 5, i * 5, comnd_cl.id, aux2, comnd_cl.descrp, comnd_cl.marque, aux);
            prix_total += comnd_cl.pau * comnd_cl.qt + comnd_cl.tva;
          }
        }
        else if (choix == 2)
        {
          i++;
          snprintf(aux, 30, "%f", comnd_cl.pau);
          snprintf(aux2, 10, "%u", comnd_cl.qt);
          remplir_table(tab, length, 5, i * 5, comnd_cl.id, aux2, comnd_cl.descrp, comnd_cl.marque, aux);
          prix_total += comnd_cl.pau * comnd_cl.qt + comnd_cl.tva;
        }
      }
    }
    print_table(tab, length, i + 1, 5);
    printf("Prix total: %f\n", prix_total + mag.timb * (1 && prix_total));
  }
}