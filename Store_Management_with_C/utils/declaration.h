#ifndef DECLARATION_H
#define DECLARATION_H

typedef struct
{
  char nom[30], adresse[50], fax[20], tel[10];
  short unsigned timb;
} magasin;

typedef struct
{
  char id[20], descrp[50], marque[40];
  unsigned int qt, en_arrivage, qt_en_att;
  float pau, pvu, tva;
} produit;

typedef struct
{
  unsigned int jj, mm, an;
} date;

typedef struct
{
  char nom[30], prenom[30], tel[10], adresse[50], email[30], pays[30], fonction[30], societe[30], mdp[30];
  date dn;
} client;

typedef struct
{
  unsigned int qt;
  char num[20], nom[20], id[20];
  date da;
  float pu, pt;
} facture;

typedef struct
{
  char nom[30], prenom[30], tel[10], adresse[50], email[30], pays[30], fonction[30], societe[30], mdp[30];
  produit prod[100];
  unsigned npr;
} fournisseur;

typedef struct
{
  char id[20], tel_fo[10];
  unsigned qt, validee;
  date dach, dliv;
} commande_gest;

typedef struct
{
  char id[20], tel[10], nom[30], prenom[30], descrp[50], marque[40];
  unsigned qt;
  float pau, tva;
  date dach, dliv;
} commande_client;

extern long unsigned int size_cl, size_mag, size_prod, size_fact, size_fo, size_comnd_cl, size_comnd_gest;
extern char* informations[9], * magasin_informations[5], * produit_informations[7], * facture_informations[7];
extern const char* bold, * underlined, * red, * green, * yellow, * blue, * magenta, * cyan, * white, * bright_red, * bright_green, * bright_yellow, * bright_blue, * bright_magenta, * bright_cyan, * bright_white;
#endif