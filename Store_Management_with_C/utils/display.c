#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include "declaration.h"

void repeter_carac(char* s, int n, char c)
{
  for (int i = 0; i < n; i++)
  {
    s[i] = c;
  }
  s[n] = '\0';
}

void remplir_table(char** tab, int* length, int n, int start, ...)
{
  va_list args;
  va_start(args, start);

  // Loop through the arguments to assign values
  for (int i = start; i < start + n; i++)
  {
    tab[i] = malloc(200);

    strcpy(tab[i], va_arg(args, char*));

    if (strlen(tab[i]) > length[i % n]) {
      length[i % n] = strlen(tab[i]);
    }
  }

  va_end(args);
}

void print_table(char** tab, int* length, int l, int c)
{
  int i, j, k;
  char aux[150];
  for (i = 0; i < l; i++)
  {
    for (k = 0; k < c; k++)
    {
      repeter_carac(aux, length[k] + 2, '-');
      printf("+%s", aux);
    }
    printf("+\n|");
    for (j = 0 + i * c; j < (i + 1) * c; j++)
    {
      // printf("%d", length[j % c]);
      repeter_carac(aux, length[j % c] - strlen(tab[j]), ' ');
      // printf("\nj = %d\n", j);
      printf(" %s %s|", tab[j], aux);
    }
    printf("\n");
  }
  for (k = 0; k < c; k++)
  {
    repeter_carac(aux, length[k] + 2, '-');
    printf("+%s", aux);
  }
  printf("+\n");
}

void print_client(client cl, char** tab, int* length, int start)
{
  char aux[15];
  snprintf(aux, 15, "%u/%u/%u", cl.dn.jj, cl.dn.mm, cl.dn.an);
  remplir_table(tab, length, 9, start, cl.prenom, cl.nom, cl.tel, cl.adresse, cl.email, cl.pays, cl.fonction, cl.societe, aux);
}

void print_produit(produit pr, char** tab, int* length, int start, short en_arrivage)
{
  char aux[15], aux2[30], aux3[30], aux4[30];
  if (en_arrivage) {
    snprintf(aux, 15, "%u", pr.qt_en_att);
  }
  else {
    snprintf(aux, 15, "%u", pr.qt);
  }
  snprintf(aux2, 30, "%f", pr.pau);
  snprintf(aux3, 30, "%f", pr.pvu);
  snprintf(aux4, 30, "%f", pr.tva);
  remplir_table(tab, length, 7, start, pr.id, pr.descrp, pr.marque, aux, aux2, aux3, aux4);
}

void print_fournisseur(fournisseur fo, char** tab, int* length, int start)
{
  remplir_table(tab, length, 8, start, fo.prenom, fo.nom, fo.tel, fo.adresse, fo.email, fo.pays, fo.fonction, fo.societe);
  printf("Les produits du fournisseur qui a le tel: '%s'\n", fo.tel);
  char** tab2 = malloc(150 * sizeof(char*));
  int length2[7] = { 0 };
  remplir_table(tab2, length2, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
  for (int i = 0; i < fo.npr; i++)
  {
    print_produit(fo.prod[i], tab2, length2, (i + 1) * 7, 0);
  }
  print_table(tab2, length2, fo.npr + 1, 7);
}

short print_magasin(char* file_name)
{
  magasin mag;
  FILE* file = fopen(file_name, "rb");
  fread(&mag, size_mag, 1, file);
  char** tab = malloc(12 * sizeof(char*));
  int length[5] = { 0 };
  char aux[7];
  snprintf(aux, 7, "%d", mag.timb);
  remplir_table(tab, length, 5, 0, "Nom", "Numero de telephone", "Adresse", "Fax", "Timbre fascal");
  remplir_table(tab, length, 5, 5, mag.nom, mag.tel, mag.adresse, mag.fax, aux);
  print_table(tab, length, 2, 5);
  return mag.timb;
}

void afficher_list_ordonee(char** p, int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("%d. %s\n", i + 1, p[i]);
  }
}

void afficher_list_client(client* arr_cl, int n)
{
  char** tab = malloc(100 * sizeof(char*));
  int length[9] = { 0 };
  remplir_table(tab, length, 9, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe", "Date de naissance");
  for (int i = 0; i < n; i++)
  {
    print_client(arr_cl[i], tab, length, (i + 1) * 9);
  }
  print_table(tab, length, n + 1, 9);
}

void afficher_list_fournisseur(fournisseur* arr_fo, int n)
{
  char** tab = malloc(100 * sizeof(char*));
  int length[8] = { 0 };
  remplir_table(tab, length, 8, 0, "Prenom", "Nom", "Numero de telephone", "Adresse", "Email", "Pays", "Fonction", "Societe");
  for (int i = 0; i < n; i++)
  {
    print_fournisseur(arr_fo[i], tab, length, (i + 1) * 8);
  }
  print_table(tab, length, n + 1, 8);
}

void afficher_list_produit(produit* arr_pr, int n)
{
  char** tab = malloc(100 * sizeof(char*));
  int length[7] = { 0 };
  remplir_table(tab, length, 7, 0, "ID", "Description", "Marque", "Quantite", "Prix d'achat unitaire", "Prix de vente unitaire", "TVA");
  for (int i = 0; i < n; i++)
  {
    print_produit(arr_pr[i], tab, length, (i + 1) * 7, 0);
  }
  print_table(tab, length, n + 1, 7);
}

void colored_text(char* text, const char* color, const char* bd, const char* ud)
{
  printf("\033[%s%s%sm%s\033[0m", color, bd, ud, text);
}
// int main()
// {
//   int rows = 10, columns = 100;
//   char **tab = malloc(rows * sizeof(char *));
//   int length[5] = {0};
//   remplir_table(tab, length, 3, 0, "Prenom", "Nom", "Tel");
//   remplir_table(tab, length, 3, 3, "Yassine", "Ghoudi", "94554292");
//   remplir_table(tab, length, 3, 6, "Mohamed", "Hajjej", "22333456");
//   remplir_table(tab, length, 3, 9, "Ahmed", "Kammoun", "22333456");
//   print_table(tab, length, 4, 3);
//   colored_text("Yassine Ghoudi\n", bright_red, bold, underlined);
// }
