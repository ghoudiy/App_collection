#include <stdio.h>
#include <time.h>
#include <string.h>
#include "../../utils/declaration.h"
#include "../../utils/common.h"
#include "../../utils/recherche.h"
#include "../../utils/input.h"
#include "../../utils/display.h"
#include "fournisseur.h"

void passer_commande(char* ffo, char* fcomnd_gest)
{
  fournisseur arr_fo[100];
  commande_gest comnd_gest;
  int nfo;
  chargerTabFournisseur(ffo, arr_fo, &nfo);
  int p = pos_fournisseur(arr_fo, nfo, "\nDonner le numero du telephone du fournisseur: ", ffo);

  do
  {
    saisie_v2(comnd_gest.id, "Donner l'id du produit qui vous voulez l'acheter: ", white, "", "");
  } while (recherche_produit(arr_fo[p].prod, arr_fo[p].npr, comnd_gest.id) == -1);
  comnd_gest.qt = saisie_int(1, 1000, "Donner la quantite du produit voulu: ", white, "", "");

  time_t t = time(NULL);
  struct tm now = *localtime(&t);
  comnd_gest.dach.jj = now.tm_mday;
  comnd_gest.dach.mm = now.tm_mon + 1;
  comnd_gest.dach.an = now.tm_year + 1900;

  comnd_gest.validee = 0;

  strcpy(comnd_gest.tel_fo, arr_fo[p].tel);

  FILE* file = fopen(fcomnd_gest, "ab");
  fwrite(&comnd_gest, size_comnd_gest, 1, file);
  fclose(file);
  colored_text("La commande a été effectué avec succès !\n", bright_green, "", "");
}
