#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "declaration.h"
#include "input.h"
#include "recherche.h"
#include "display.h"

void chargerTabClient(char* file_name, client* array_client, int* n)
{
  FILE* file = fopen(file_name, "rb");
  if (file != NULL)
  {
    *n = 0;
    while (fread(&array_client[*n], size_cl, 1, file) == 1)
    {
      (*n)++;
    }
    fclose(file);
  }
}

void chargerTabFournisseur(char* file_name, fournisseur* array_fournisseur, int* n)
{
  FILE* file = fopen(file_name, "rb");
  if (file != NULL)
  {
    *n = 0;
    while (fread(&array_fournisseur[*n], size_fo, 1, file) == 1)
    {
      (*n)++;
    }
    fclose(file);
  }
}

void chargerTabProduit(char* file_name, produit* array_produit, int* n)
{
  FILE* file = fopen(file_name, "rb");
  if (file != NULL)
  {
    *n = 0;
    while (fread(&array_produit[*n], size_prod, 1, file) == 1)
    {
      (*n)++;
    }
    fclose(file);
  }
}

void chargerTabCommandeCl(char* file_name, commande_client* array_commande, int* n)
{
  FILE* file = fopen(file_name, "rb");
  if (file != NULL)
  {
    *n = 0;
    while (fread(&array_commande[*n], size_comnd_cl, 1, file) == 1)
    {
      (*n)++;
    }
    fclose(file);
  }
}

void chargerTabCommandeGest(char* file_name, commande_gest* array_commande, int* n)
{
  FILE* file = fopen(file_name, "rb");
  if (file != NULL)
  {
    *n = 0;
    while (fread(&array_commande[*n], size_comnd_gest, 1, file) == 1)
    {
      (*n)++;
    }
    fclose(file);
  }
}

void remplirFichClient(char* file_name, client* arr_cl, int n)
{
  FILE* file = fopen(file_name, "wb");
  fwrite(arr_cl, size_cl, n, file);
  fclose(file);
}

void remplirFichFournisseur(char* file_name, fournisseur* arr_fo, int n)
{
  FILE* file = fopen(file_name, "wb");
  fwrite(arr_fo, size_fo, n, file);
  fclose(file);
}

void remplirFichProduit(char* file_name, produit* arr_pr, int n)
{
  FILE* file = fopen(file_name, "wb");
  fwrite(arr_pr, size_prod, n, file);
  fclose(file);
}

int ajouter_client(char* file_name)
{
  int n;
  client cl, arr_cl[100];
  const int days[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

  chargerTabClient(file_name, arr_cl, &n);

  saisie(cl.nom, "Nom: ", 'a', 'z', bright_white, "", "");
  saisie(cl.prenom, "Prenom: ", 'a', 'z', bright_white, "", "");

  // L'identifiant du client est son numero de telephone, c'est pourquoi nous verifions l'unicite du numero
  do
  {
    saisie(cl.tel, "Numero de telephone: ", '0', '9', bright_white, "", "");
  } while (recherche_tel_client(arr_cl, n, cl.tel) != -1 || strlen(cl.tel) != 8);

  colored_text("Adresse: ", bright_white, "", "");
  scanf("%s", cl.adresse);

  do
  {
    saisie_email(cl.email, "Email: ", bright_white, "", "");
  } while (recherche_email_client(arr_cl, n, cl.email) != -1);

  saisie(cl.pays, "Pays: ", 'a', 'z', bright_white, "", "");
  saisie(cl.fonction, "Fonction: ", 'a', 'z', bright_white, "", "");
  saisie(cl.societe, "Societe: ", 'a', 'z', bright_white, "", "");

  printf("Date du naissance:\n");
  cl.dn.an = saisie_int(1910, 2024, "Annee: ", bright_white, "", "");
  cl.dn.mm = saisie_int(1, 12, "Mois: ", bright_white, "", "");
  cl.dn.jj = saisie_int(1, days[cl.dn.mm - 1] + 1 * (cl.dn.an % 4 == 0 && cl.dn.mm == 2), "Jour: ", bright_white, "", "");

  do {
    colored_text("Mot de passe: ", bright_white, "", "");
    scanf("%s", cl.mdp);
  } while (strlen(cl.mdp) < 6);

  FILE* file = fopen(file_name, "ab");

  if (file == NULL) {
    colored_text("Erreurs lors l'ouverture du fichier", bright_red, "", "");
    return 1;
  }

  fwrite(&cl, sizeof(client), 1, file);
  fclose(file);
  return 0;
}

void ajouter_produit(produit* pr, char* file_name, char* marque)
{
  int n;
  produit arr_pr[100];
  chargerTabProduit(file_name, arr_pr, &n);

  do
  {
    saisie_v2((*pr).id, "ID: ", bright_white, "", "");
  } while (recherche_produit(arr_pr, n, (*pr).id) != -1);

  saisie_v2((*pr).descrp, "Description: ", bright_white, "", "");
  if (strlen(marque) == 0) {
    saisie_v2((*pr).marque, "Marque: ", bright_white, "", "");
  }
  else {
    strcpy((*pr).marque, marque);
  }

  (*pr).qt = saisie_int(1, 1000, "Quantite: ", bright_white, "", "");
  (*pr).pau = saisie_float(0.1, 10000, "Prix d'achat unitaire: ", bright_white, "", "");
  (*pr).pvu = saisie_float(0.1, 10000, "Prix de vente unitaire: ", bright_white, "", "");
  (*pr).tva = saisie_float(0.1, 50, "TVA: ", bright_white, "", "");
  (*pr).en_arrivage = 0;
}

int ajouter_fournisseur(char* ffo, char* fpr)
{
  int n;
  fournisseur fo, arr_fo[100];

  chargerTabFournisseur(ffo, arr_fo, &n);

  saisie(fo.nom, "Nom: ", 'a', 'z', bright_white, "", "");
  saisie(fo.prenom, "Prenom: ", 'a', 'z', bright_white, "", "");

  // L'identifiant du fournisseur est son numero de telephone, c'est pourquoi nous verifions l'unicite du numero
  do
  {
    saisie(fo.tel, "Numero de telephone: ", '0', '9', bright_white, "", "");
  } while (recherche_tel_fournisseur(arr_fo, n, fo.tel) != -1 || strlen(fo.tel) != 8);

  colored_text("Adresse: ", bright_white, "", "");
  scanf("%s", fo.adresse);

  do
  {
    saisie_email(fo.email, "Email: ", bright_white, "", "");
  } while (recherche_email_fournisseur(arr_fo, n, fo.email) != -1);

  saisie(fo.pays, "Pays: ", 'a', 'z', bright_white, "", "");
  saisie(fo.fonction, "Fonction: ", 'a', 'z', bright_white, "", "");
  do
  {
    saisie_v2(fo.societe, "Societe: ", bright_white, "", "");
  } while (recherche_societe_fournisseur(arr_fo, n, fo.societe) != -1);

  do {
    colored_text("Mot de passe: ", bright_white, "", "");
    scanf("%s", fo.mdp);
  } while (strlen(fo.mdp) < 6);

  fo.npr = saisie_int(1, 100, "Nombre de produit: ", bright_white, "", "");
  for (int i = 0; i < fo.npr; i++)
  {
    ajouter_produit(&fo.prod[i], fpr, fo.societe);
  }

  FILE* file = fopen(ffo, "ab");
  if (file == NULL)
  {
    perror("Erreurs lors l'ouverture du fichier");
    return 1;
  }
  fwrite(&fo, size_fo, 1, file);
  fclose(file);
  return 0;
}

int comparer_date(struct tm now, date d2)
{
  return (now.tm_year > d2.an) ||
    (now.tm_year == d2.an && now.tm_mon > d2.mm) ||
    (now.tm_year == d2.an && now.tm_mon == d2.mm && now.tm_mday > d2.jj);
}

int comparer_date_v2(date d1, date d2)
{
  return (d1.an > d2.an) ||
    (d1.an == d2.an && d1.mm > d2.mm) ||
    (d1.an == d2.an && d1.mm == d2.mm && d1.jj > d2.jj);
}

void mise_a_jour_donnee(char* fcomnd_gest, char* ffo, char* fpr) {
  commande_gest comnd[100];
  int p, ncg, npr, p2, nfo, p3;
  produit arrpr[200];
  fournisseur arrfo[100];
  chargerTabCommandeGest(fcomnd_gest, comnd, &ncg);
  chargerTabFournisseur(ffo, arrfo, &nfo);
  chargerTabProduit(fpr, arrpr, &npr);
  time_t t = time(NULL);
  struct tm now = *localtime(&t);
  for (int i = 0; i < ncg; i++)
  {
    if (comparer_date(now, comnd[i].dliv) == 1) {
      p = recherche_produit(arrpr, npr, comnd[i].id);
      p2 = recherche_tel_fournisseur(arrfo, nfo, comnd[i].tel_fo);
      p3 = recherche_produit(arrfo[p2].prod, arrfo[p2].npr, comnd[i].id);
      arrpr[p].en_arrivage = 0;
      arrpr[p].qt_en_att += comnd[i].qt;
      arrfo[p2].prod[p3].qt -= comnd[i].qt;
    }
  }
  FILE* file = fopen(fpr, "wb");
  fwrite(arrpr, size_prod, npr, file);
  fclose(file);

  file = fopen(ffo, "wb");
  fwrite(arrfo, size_fo, nfo, file);
  fclose(file);
}

void verifier_mdp(char* msg, char* mdp, char* correct_mdp, const char* color, const char* bold, const char* underline) {
  int max_try = 3;
  do {
    colored_text(msg, color, bold, underline);
    scanf("%s", mdp);
    max_try--;
  } while (strcmp(correct_mdp, mdp) != 0 && max_try > 0);

  if (max_try == 0) {
    colored_text("\nVous avez atteint le nombre maximum d'essais\n", bright_red, "", "");
    exit(1);
  }
}