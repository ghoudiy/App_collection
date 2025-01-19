#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../../utils/recherche.h"
#include "../../utils/input.h"
#include "../../utils/common.h"
#include "../../utils/display.h"
#include "../../utils/declaration.h"

void ajouter_fournisseur_gest(char* ffo, char* fpr)
{
  if (ajouter_fournisseur(ffo, fpr) == 0)
  {
    colored_text("Le fournisseur a été ajouté avec succès.", green, bold, underlined);
  }
  else
  {
    colored_text("Une erreur se produise lors de l'ajout", bright_red, "", "");
  }
}

int rechercher_fournisseur_gest(char* msg, short change, fournisseur* arrf, int* narrf, fournisseur* foc, int ub, char* ffo)
{
  int narr, narr2, narr3, j, n, p;
  fournisseur arr_fo[100], arr[100];
  char tel[10], nom[30], prenom[30], email[30], societe[30];
  chargerTabFournisseur(ffo, arr_fo, &n);

  if (strlen(msg) > 0)
  {
    printf("%s", msg);
  }
  else
  {
    colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche", bright_blue, "", "");
    printf("\n1. Nom\n2. Prénom\n3. Nom et Prénom\n4. Societe\n5. Téléphone\n6. Email:");
  }

  int choix;
  ub += 6 * (!ub);
  char message[30];
  snprintf(message, 30, "\nEntrez votre choix (1-%d): ", ub);
  choix = saisie_int(1, ub, message, bright_yellow, "", "");
  switch (choix)
  {
  case 1:
    saisie(nom, "Donner le nom du fournisseur a chercher: ", 'a', 'z', white, "", "");
    recherche_nom_fournisseur(arr_fo, n, nom, arr, &narr);
    if (narr > 0)
    {
      afficher_list_fournisseur(arr, narr);
      if (change)
      {
        memcpy(arrf, arr, sizeof(arr));
        *narrf = narr;
      }
      return 1;
    }
    else
      colored_text("Le nom est incorrect ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;

  case 2:
    saisie(prenom, "Donner le prenom du fournisseur a chercher: ", 'a', 'z', white, "", "");
    recherche_prenom_fournisseur(arr_fo, n, prenom, arr, &narr);
    if (narr > 0)
    {
      afficher_list_fournisseur(arr, narr);
      if (change)
      {
        memcpy(arrf, arr, sizeof(arr));
        *narrf = narr;
      }
      return 1;
    }
    else
      colored_text("Le prenom est incorrect ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;

  case 3:
    fournisseur arr2[100], arr3[100];
    saisie(nom, "Donner le nom du fournisseur a chercher: ", 'a', 'z', white, "", "");
    recherche_nom_fournisseur(arr_fo, n, nom, arr2, &narr2);

    saisie(prenom, "Donner le prenom du fournisseur a chercher: ", 'a', 'z', white, "", "");
    recherche_prenom_fournisseur(arr_fo, n, prenom, arr3, &narr3);

    narr = 0;
    for (int i = 0; i < narr2; i++)
    {
      j = -1;
      do
      {
        j++;
      } while (strcmp(arr2[i].tel, arr3[j].tel) != 0 && j < narr3 - 1);
      if (strcmp(arr2[i].tel, arr3[j].tel) == 0)
      {
        arr[narr] = arr2[i];
        narr++;
      }
    }
    if (narr > 0)
    {
      afficher_list_fournisseur(arr, narr);
      if (change)
      {
        memcpy(arrf, arr, sizeof(arr));
        *narrf = narr;
      }
      return 1;
    }
    else
      colored_text("Le nom et prenom sont incorrectes ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;

  case 4:
    saisie_v2(societe, "Donner le nom du societe (du fournisseur) a chercher: ", white, "", "");

    if ((p = recherche_societe_fournisseur(arr_fo, n, societe)) != -1)
    {
      char** tab = malloc(100 * sizeof(char*));
      int length[8] = { 0 };
      remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
      print_fournisseur(arr_fo[p], tab, length, 8);
      print_table(tab, length, 2, 8);
      if (change)
        *foc = arr_fo[p];
      return 1;
    }
    else
      colored_text("Le nom du societe est incorrect ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;

  case 5:
    saisie(tel, "Donner le numero de telephone du fournisseur a chercher: ", '0', '9', white, "", "");
    if ((p = recherche_tel_fournisseur(arr_fo, n, tel)) != -1)
    {
      char** tab = malloc(100 * sizeof(char*));
      int length[8] = { 0 };
      remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
      print_fournisseur(arr_fo[p], tab, length, 8);
      print_table(tab, length, 2, 8);
      if (change)
        *foc = arr_fo[p];
      return 1;
    }
    else
      colored_text("Le numero de telephone est incorrect ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;

  case 6:
    saisie_email(email, "Donner l'email du fournisseur a chercher: ", white, "", "");
    if ((p = recherche_email_fournisseur(arr_fo, n, email)) != -1)
    {
      char** tab = malloc(100 * sizeof(char*));
      int length[8] = { 0 };
      remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
      print_fournisseur(arr_fo[p], tab, length, 8);
      print_table(tab, length, 2, 8);
      if (change)
        *foc = arr_fo[p];
      return 1;
    }
    else
      colored_text("L'email est incorrect ou le fournisseur n'est existe pas\n", bright_red, "", "");
    break;
  }
  return 0;
}

int pos_fournisseur(fournisseur* arr_fo, int n, char* msg, char* ffo)
{
  int p;
  char tel[10], aux[100];
  strcpy(aux, msg);
  strcat(aux, "(Taper 0 si tu oublies le tel): ");
  saisie(tel, aux, '0', '9', bright_yellow, "", "");
  if (strcmp(tel, "0") == 0)
  {
    do
    {
      colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche", bright_blue, "", "");
    } while (rechercher_fournisseur_gest("\n1. Nom\n2. Prenom\n3. Nom et Prenom\n4. Societe", 0, NULL, NULL, NULL, 4, ffo) == 0);
    saisie(tel, msg, '0', '9', white, "", "");
  }
  do {
    p = recherche_tel_fournisseur(arr_fo, n, tel);
    if (p == -1) {
      colored_text("Ce numero est introuvable\n", bright_red, "", "");
      saisie(tel, msg, '0', '9', white, "", "");
    }
  } while (p == -1);
  return p;
}

void modifier_fournisseur_gest(char* ffo)
{
  char tel[10], societe[30], email[30];
  int choix, n, p;
  fournisseur arr_fo[100];
  chargerTabFournisseur(ffo, arr_fo, &n);
  p = pos_fournisseur(arr_fo, n, "\nDonner le numero du telephone du fournisseur a modifier: ", ffo);

  afficher_list_ordonee(informations, 9);
  choix = saisie_int(1, 9, "Souhaitez-vous modifier le? ", bright_cyan, "", "");
  switch (choix)
  {
  case 1:
    saisie(arr_fo[p].nom, "Veuillez introduire le nouveau nom: ", 'a', 'z', bright_white, "", "");
    break;
  case 2:
    saisie(arr_fo[p].prenom, "Veuillez introduire le nouveau prenom: ", 'a', 'z', bright_white, "", "");
    break;
  case 3:
    do
    {
      saisie(tel, "Veuillez introduire le nouveau tel: ", '0', '9', bright_white, "", "");
    } while (recherche_tel_fournisseur(arr_fo, n, tel) != -1);
    strcpy(arr_fo[p].tel, tel);
    break;
  case 4:
    do
    {
      saisie_email(tel, "Veuillez introduire le nouveau email: ", bright_white, "", "");
    } while (recherche_email_fournisseur(arr_fo, n, email) != -1);
    strcpy(arr_fo[p].email, email);
    break;
  case 5:
    colored_text("Veuillez introduire la nouveau adresse: ", bright_white, "", "");
    scanf("%s", arr_fo[p].adresse);
    break;
  case 6:
    saisie(arr_fo[p].pays, "Veuillez introduire le nouveau pays: ", 'a', 'z', bright_white, "", "");
    break;
  case 7:
    saisie(arr_fo[p].fonction, "Veuillez introduire la nouveau fonction: ", 'a', 'z', bright_white, "", "");
    break;
  case 8:
    do
    {
      saisie_v2(societe, "Veuillez introduire la nouveau societe: ", bright_white, "", "");
    } while (recherche_societe_fournisseur(arr_fo, n, societe) != -1);
    strcpy(arr_fo[p].societe, societe);
    break;
  case 9:
    saisie(arr_fo[p].mdp, "Veuillez introduire le nouveau mot de passe: ", 'a', 'z', bright_white, "", "");
    break;
  }
  remplirFichFournisseur(ffo, arr_fo, n);
}

void supprimer_fournisseur_gest(char* ffo)
{
  fournisseur arr_fo[100];
  int n = 0, p;
  chargerTabFournisseur(ffo, arr_fo, &n);

  p = pos_fournisseur(arr_fo, n, "\nDonner le numero du telephone du fournisseur a supprimer: ", ffo);
  FILE* file = fopen(ffo, "wb");
  for (int i = 0; i < n; i++)
  {
    if (i != p)
    {
      fwrite(&arr_fo[i], size_fo, 1, file);
    }
  }
  fclose(file);
}

void afficher_fournisseur_gest(char* ffo)
{
  FILE* file = fopen(ffo, "rb");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
  }
  else
  {
    char** tab = malloc(100 * sizeof(char*));
    int length[8] = { 0 }, ntab = 1;
    remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
    fournisseur fo;
    while (fread(&fo, size_fo, 1, file) == 1)
    {
      print_fournisseur(fo, tab, length, ntab * 8);
      ntab++;
    }
    print_table(tab, length, ntab, 8);
  }
  fclose(file);
}

// int main()
// {
//   ajouter_fournisseur_gest(char *ffo);
//   rechercher_fournisseur_gest(char* msg, short change, fournisseur* arrf, int* narrf, fournisseur* foc, int ub);
//   modifier_fournisseur_gest(char *ffo);
//   supprimer_fournisseur_gest(char *ffo);
//   afficher_fournisseur_gest(char *ffo);
// }