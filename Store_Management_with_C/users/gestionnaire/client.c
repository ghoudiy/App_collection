#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utils/recherche.h"
#include "../../utils/input.h"
#include "../../utils/common.h"
#include "../../utils/display.h"
#include "../../utils/declaration.h"
void ajouter_client_gest(char* fcl)
{
  if (ajouter_client(fcl) == 0)
  {
    colored_text("Le client a été ajouté avec succès\n", green, bold, underlined);
  }
  else
  {
    colored_text("Une erreur se produise lors de l'ajout\n", red, bold, "");
  }
}

int rechercher_client_gest(char* msg, short change, client* arrc, int* narrc, client* clc, int ub, char* fcl)
{
  int narr, narr2, narr3, j, n, p;
  client arr_cl[100], arr[100];
  char tel[10], nom[30], prenom[30], email[30];
  chargerTabClient(fcl, arr_cl, &n);

  if (strlen(msg) > 0)
  {
    printf("%s", msg);
  }
  else
  {
    colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche :", bright_blue, "", "");
    printf("\n1. Nom\n2. Prénom\n3. Nom et Prénom\n4. Téléphone\n5. Email");
  }

  int choix;
  ub += 5 * (!ub);
  char message[30];
  snprintf(message, 30, "\nEntrez votre choix (1-%d): ", ub);
  choix = saisie_int(1, ub, message, yellow, "", "");
  switch (choix)
  {
  case 1:
    saisie(nom, "Donner le nom du client a chercher: ", 'a', 'z', white, "", "");
    recherche_nom_client(arr_cl, n, nom, arr, &narr);
    if (narr > 0)
    {
      afficher_list_client(arr, narr);
      if (change)
      {
        memcpy(arrc, arr, sizeof(arr));
        *narrc = narr;
      }
      return 1;
    }
    else
      colored_text("Le nom est incorrect ou le client n'est existe pas\n", bright_red, "", "");
    break;

  case 2:
    saisie(prenom, "Donner le prenom du client a chercher: ", 'a', 'z', white, "", "");
    recherche_prenom_client(arr_cl, n, prenom, arr, &narr);
    if (narr > 0)
    {
      afficher_list_client(arr, narr);
      if (change)
      {
        memcpy(arrc, arr, sizeof(arr));
        *narrc = narr;
      }
      return 1;
    }
    else
      colored_text("Le prenom est incorrect ou le client n'est existe pas\n", bright_red, "", "");
    break;

  case 3:
    client arr2[100], arr3[100];
    saisie(nom, "Donner le nom du client a chercher: ", 'a', 'z', white, "", "");
    recherche_nom_client(arr_cl, n, nom, arr2, &narr2);

    saisie(prenom, "Donner le prenom du client a chercher: ", 'a', 'z', white, "", "");
    recherche_prenom_client(arr_cl, n, prenom, arr3, &narr3);

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
      afficher_list_client(arr, narr);
      if (change)
      {
        memcpy(arrc, arr, sizeof(arr));
        *narrc = narr;
      }
      return 1;
    }
    else
      colored_text("Le nom et prenom sont incorrectes ou le client n'est existe pas\n", bright_red, "", "");
    break;

  case 4:
    saisie(tel, "Donner le numero de telephone du client a chercher: ", '0', '9', white, "", "");
    if ((p = recherche_tel_client(arr_cl, n, tel)) != -1)
    {
      char** tab = malloc(100 * sizeof(char*));
      int length[9] = { 0 };
      remplir_table(tab, length, 9, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe", "Date de naissance");
      print_client(arr_cl[p], tab, length, 9);
      print_table(tab, length, 2, 9);
      if (change)
        *clc = arr_cl[p];
      return 1;
    }
    else
      colored_text("Le numero de telephone est incorrect ou le client n'est existe pas\n", bright_red, "", "");
    break;

  case 5:
    saisie_email(email, "Donner l'email du client a chercher: ", white, "", "");
    if ((p = recherche_email_client(arr_cl, n, email)) != -1)
    {
      char** tab = malloc(100 * sizeof(char*));
      int length[9] = { 0 };
      remplir_table(tab, length, 9, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe", "Date de naissance");
      print_client(arr_cl[p], tab, length, 9);
      print_table(tab, length, 2, 9);
      if (change)
        *clc = arr_cl[p];
      return 1;
    }
    else
      colored_text("L'email est incorrect ou le client n'est existe pas\n", bright_red, "", "");
    break;
  }

  return 0;
}

int pos_client(client* arr_cl, int n, char* msg, char* fcl)
{
  int p;
  char tel[10], aux[100];
  strcpy(aux, msg);
  strcat(aux, "(Taper 0 si tu oublies le tel): ");
  saisie(tel, aux, '0', '9', magenta, bold, "");
  if (strcmp(tel, "0") == 0)
  {
    do
    {
      colored_text("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche", bright_blue, "", "");
    } while (rechercher_client_gest("\n1. Nom\n2. Prenom\n3. Nom et Prenom", 0, NULL, NULL, NULL, 3, fcl) == 0);
    saisie(tel, msg, '0', '9', white, "", "");
  }
  do {
    p = recherche_tel_client(arr_cl, n, tel);
    if (p == -1) {
      colored_text("Ce numero est introuvable\n", bright_red, "", "");
      saisie(tel, msg, '0', '9', white, "", "");
    }
  } while (p == -1);
  return p;
}

void modifier_client_gest(char* fcl)
{
  char tel[10], email[30];
  int choix, n, p;
  client arr_cl[100];
  chargerTabClient(fcl, arr_cl, &n);
  p = pos_client(arr_cl, n, "\nDonner le numero du telephone du client a modifier ", fcl);

  afficher_list_ordonee(informations, 8);
  choix = saisie_int(1, 8, "Souhaitez-vous modifier le? ", bright_cyan, "", "");
  switch (choix)
  {
  case 1:
    saisie(arr_cl[p].nom, "Veuillez introduire le nouveau nom: ", 'a', 'z', bright_white, "", "");
    break;
  case 2:
    saisie(arr_cl[p].prenom, "Veuillez introduire le nouveau prenom: ", 'a', 'z', bright_white, "", "");
    break;
  case 3:
    do
    {
      saisie(tel, "Veuillez introduire le nouveau tel: ", '0', '9', bright_white, "", "");
    } while (recherche_tel_client(arr_cl, n, tel) != -1);
    strcpy(arr_cl[p].tel, tel);
    break;
  case 4:
    do
    {
      saisie_email(email, "Veuillez introduire le nouveau email: ", bright_white, "", "");
    } while (recherche_email_client(arr_cl, n, email) != -1);
    strcpy(arr_cl[p].email, email);
    break;
  case 5:
    colored_text("Veuillez introduire la nouveau adresse: ", bright_white, "", "");
    scanf("%s", arr_cl[p].adresse);
    break;
  case 6:
    saisie(arr_cl[p].pays, "Veuillez introduire le nouveau pays: ", 'a', 'z', bright_white, "", "");
    break;
  case 7:
    saisie(arr_cl[p].fonction, "Veuillez introduire la nouveau fonction: ", 'a', 'z', bright_white, "", "");
    break;
  case 8:
    saisie(arr_cl[p].societe, "Veuillez introduire la nouveau societe: ", 'a', 'z', bright_white, "", "");
    break;
  case 9:
    saisie(arr_cl[p].mdp, "Veuillez introduire le nouveau mot de passe: ", 'a', 'z', bright_white, "", "");
    break;
  }
  remplirFichClient(fcl, arr_cl, n);
  colored_text("Les infomrations du client sont modifiees avec success !\n", bright_green, "", "");
}

void supprimer_client_gest(char* fcl)
{
  client arr_cl[100];
  int n = 0, p;
  chargerTabClient(fcl, arr_cl, &n);

  p = pos_client(arr_cl, n, "\nDonner le numero du telephone du client a supprimer ", fcl);
  FILE* file = fopen(fcl, "wb");
  for (int i = 0; i < n; i++)
  {
    if (i != p)
    {
      fwrite(&arr_cl[i], size_cl, 1, file);
    }
  }
  fclose(file);
  colored_text("Le client a ete supprime avec succes !\n", bright_yellow, "", "");
}

void afficher_client_gest(char* fcl)
{
  FILE* file = fopen(fcl, "rb");
  if (file == NULL)
  {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
  }
  else
  {
    client cl1;
    char** tab = malloc(100 * sizeof(char*));
    int length[9] = { 0 }, ntab = 1;
    remplir_table(tab, length, 9, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe", "Date de naissance");

    while (fread(&cl1, size_cl, 1, file) == 1)
    {
      print_client(cl1, tab, length, ntab * 9);
      ntab++;
    }
    print_table(tab, length, ntab, 9);
  }
  fclose(file);
}

// int main() {
//   ajouter_client_gest("h");
//   // rechercher_client_gest("Veuillez sélectionner le champ par lequel vous souhaitez effectuer la recherche\n1. Nom\n2. Prenom\n3. Nom et Prenom", 0, NULL, NULL, NULL, 3)
//   //   modifier_client_gest(fcl);
//   // supprimer_client_gest(fcl);
//   // afficher_client_gest(fcl);
//   return 0;
// }
