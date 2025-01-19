#include <stdio.h>
#include "../../utils/declaration.h"
#include "../../utils/input.h"
#include "../../utils/display.h"

int enregistrer_info_magasin(char* fmag)
{
  magasin mag;
  saisie_v2(mag.nom, "Donner le nom du magasin: ", white, "", "");
  saisie_v2(mag.adresse, "Donner l'adresse du magasin: ", white, "", "");
  saisie(mag.fax, "Donner le fax du magasin: ", '0', '9', white, "", "");
  saisie(mag.tel, "Donner le tel du magasin: ", '0', '9', white, "", "");
  mag.timb = saisie_int(1, 100000, "Donner le timb du magasin: ", white, "", "");
  FILE* file = fopen(fmag, "wb");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
    return 1;
  }
  fwrite(&mag, size_mag, 1, file);
  fclose(file);
  colored_text("Les informations sont enregistres avec success !", bright_green, "", "");
  return 0;
}

int modifier_info_magasin(char* fmag)
{
  magasin mag;
  FILE* file = fopen(fmag, "rb");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
    return 1;
  }
  fread(&mag, size_mag, 1, file);

  afficher_list_ordonee(magasin_informations, 5);
  int choix = saisie_int(1, 5, "Souhaitez-vous modifier le? ", bright_cyan, "", "");

  switch (choix)
  {
  case 1:
    saisie_v2(mag.nom, "Donner le nouveau nom du magasin: ", white, bold, "");
    break;
  case 2:
    saisie_v2(mag.adresse, "Donner le nouveau adresse du magasin: ", white, bold, "");
    break;
  case 3:
    saisie(mag.fax, "Donner le nouveau fax du magasin: ", '0', '9', white, bold, "");
    break;
  case 4:
    saisie(mag.tel, "Donner le nouveau tel du magasin: ", '0', '9', white, bold, "");
    break;
  case 5:
    mag.timb = saisie_int(1, 100000, "Donner le nouveau timb du magasin: ", white, bold, "");
    break;
  }
  file = fopen(fmag, "wb");
  if (file == NULL) {
    perror("Une erreur se produise lors d'ouverture du fichier magasin.dat");
    return 0;
  }
  fwrite(&mag, size_mag, 1, file);
  fclose(file);
  colored_text("Les informations sont modifies avec success !", bright_green, "", "");
  return 1;
}