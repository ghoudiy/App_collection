#include<stdio.h>
#include<stdlib.h>
#include "utils/input.h"
#include "utils/common.h"
#include "users/client.h"
#include "utils/display.h"
#include "utils/recherche.h"
#include "utils/declaration.h"
#include "users/fournisseur.h"
#include "users/gestionnaire.h"
#include "users/gestionnaire/client.h"
#include "users/gestionnaire/fournisseur.h"
#include "users/gestionnaire/produit.h"
#include "users/gestionnaire/commande.h"
#include "users/gestionnaire/magasin.h"
#include "users/gestionnaire/tableau_bord_stocks.h"

int main() {

  void menu_gestionnaire();
  void menu_client();
  void menu_fournisseur();

  // mise_a_jour_donnee("data/commande_gest.dat", "data/fournisseur.dat", "data/produit.dat");
  // print_magasin("data/magasin.dat");
  // exit(0);
  colored_text("\n\nBIENVENUE !\n", bright_green, bold, "");
  printf("Veuillez sélectionner le type d'utilisateur :\n\n");
  printf("    1. Gestionnaire\n");
  printf("    2. Client\n");
  printf("    3. Fournisseur\n\n");

  int type_utilisateur = saisie_int(1, 3, "Entrez votre choix (1, 2 ou 3) : ", yellow, bold, "");
  switch (type_utilisateur)
  {
  case 1:
    menu_gestionnaire();
    break;

  case 2:
    menu_client();
    break;

  case 3:
    menu_fournisseur();
    break;
  }

  return 0;
}

void menu_gestionnaire() {
  void gerer_clients();
  void gerer_fournisseurs();
  void gerer_produits();
  void consulter_tab_bord_stock();

  colored_text("\nBienvenue Admin\n", bright_blue, bold, underlined);

  FILE* file = fopen("data/gestionnaire.dat", "rb");
  if (file == NULL) {
    colored_text("Erreur Critique XO\n", bright_red, bold, underlined);
    exit(1);
  }
  char mdp_gest[30], mdp[30];
  while (fscanf(file, "%s", mdp_gest) == 1) {
  }
  printf("\nMot de passe: '%s'\n", mdp_gest); // To remove

  verifier_mdp("Entrer le mot de passe du gestionnaire: ", mdp, mdp_gest, bright_white, "", "");

  printf("\n=== Menu Gestionnaire ===\n\n");
  file = fopen("data/nouveaux_noti_gest.txt", "r");
  FILE* ff;
  char line[170];
  if (file != NULL) {
    ff = fopen("data/notifications_gest.txt", "a");
    short test;
    while (fgets(line, sizeof(line), file) != NULL) {
      if (test) {
        printf("Nouveaux notifications: \n");
        test = 0;
      }
      printf("%s", line);
      fprintf(file, "%s", line);
    }
    fclose(file);
    fclose(ff);
  }

  printf("1. Enregistrer les informations du magasin\n");
  printf("2. Modifier les informations du magasin\n");
  printf("3. Gerer les client\n");
  printf("4. Gerer les fournisseurs\n");
  printf("5. Gerer les produits\n");
  printf("6. Consulter le tableau de bord de stocks\n");
  printf("7. Passer des commandes aupres des fournisseurs\n");
  printf("8. Afficher les notifications precedentes\n");
  printf("9. Quitter\n");

  int action_gest = saisie_int(1, 9, "Entrez l'action: ", bright_cyan, "", "");
  switch (action_gest)
  {
  case 1:
    enregistrer_info_magasin("data/magasin.dat");
    break;

  case 2:
    modifier_info_magasin("data/magasin.dat");
    break;

  case 3:
    gerer_clients();
    break;

  case 4:
    gerer_fournisseurs();
    break;

  case 5:
    gerer_produits();
    break;

  case 6:
    consulter_tab_bord_stock();
    break;

  case 7:
    passer_commande("data/fournisseur.dat", "data/commande_gest.dat");
    break;

  case 8:
    ff = fopen("data/notifications_gest.txt", "r");
    while (fgets(line, sizeof(line), ff) != NULL) {
      printf("%s", line);
      fprintf(ff, "%s", line);
    }
    fclose(ff);
  case 9:
    exit(0);
  }
}

void menu_client() {
  int se_connecter_client(client*);
  void menu_actions_client(client);

  colored_text("\nBienvenue, chere client !\n\n", bright_blue, bold, underlined);
  printf("1. Se connecter\n");
  printf("2. Creer un nouveau compte\n");
  printf("3. Quitter\n");
  client cl;
  int action_cl = saisie_int(1, 3, "Entrez l'action: ", bright_magenta, "", "");
  switch (action_cl)
  {
  case 1:
    if (se_connecter_client(&cl) == 1) {
      menu_actions_client(cl);
    }
    break;

  case 2:
    if (inscription_client("data/client.dat") == 1) {
      int choix = saisie_int(1, 2, "\n1. Se connecter\n2. Quitter\n\nEntrez l'action: ", green, bold, "");
      switch (choix)
      {
      case 1:
        if (se_connecter_client(&cl) == 1)
          menu_actions_client(cl);

      case 2:
        exit(0);
      }
    }
    break;

  case 3:
    exit(0);
  }
}

void menu_fournisseur() {
  int se_connecter_fournisseur(fournisseur*);
  void menu_actions_fournisseur(fournisseur);

  colored_text("\nBienvenue, chere fournisseur !\n\n", bright_blue, bold, underlined);
  printf("1. Se connecter\n");
  printf("2. Creer un nouveau compte\n");
  printf("3. Quitter\n");
  int action_fo = saisie_int(1, 3, "Entrez l'action: ", bright_magenta, "", "");
  fournisseur fo;
  switch (action_fo)
  {
  case 1:
    if (se_connecter_fournisseur(&fo) == 1) {
      menu_actions_fournisseur(fo);
    }
    break;

  case 2:
    if (inscription_fournisseur("data/fournisseur.dat", "data/produit.dat") == 1) {
      int choix = saisie_int(1, 2, "\n1. Se connecter\n2. Quitter\n\nEntrez l'action: ", green, bold, "");
      switch (choix)
      {
      case 1:
        if (se_connecter_fournisseur(&fo) == 1)
          menu_actions_fournisseur(fo);
      case 2:
        exit(0);
      }
    }
    break;

  case 3:
    exit(0);
  }
}

void gerer_clients() {
  printf("\n\n=== Gerer les clients ===\n");
  printf("1. Ajouter un nouveau client\n");
  printf("2. Modifer les informations d'un client\n");
  printf("3. Supprimer un client\n");
  printf("4. Rechercher un client\n");
  printf("5. Afficher les clients\n");

  int action_gest_cl = saisie_int(1, 5, "Entrez l'action: ", bright_green, "", "");

  switch (action_gest_cl)
  {

  case 1:
    ajouter_client_gest("data/client.dat");
    break;

  case 2:
    modifier_client_gest("data/client.dat");
    break;

  case 3:
    supprimer_client_gest("data/client.dat");
    break;

  case 4:
    rechercher_client_gest("", 0, NULL, NULL, NULL, 0, "data/client.dat");
    break;

  case 5:
    afficher_client_gest("data/client.dat");
    break;
  }
}

void gerer_fournisseurs() {
  printf("\n\n=== Gerer les fournisseurs ===\n");
  printf("1. Ajouter un nouveau fournisseur\n");
  printf("2. Modifer les informations d'un fournisseur\n");
  printf("3. Supprimer un fournisseur\n");
  printf("4. Rechercher un fournisseur\n");
  printf("5. Afficher les fournisseurs\n");

  int action_gest_fo = saisie_int(1, 5, "Entrez l'action: ", bright_green, "", "");

  switch (action_gest_fo)
  {

  case 1:
    ajouter_fournisseur_gest("data/fournisseur.dat", "data/produit.dat");
    break;

  case 2:
    modifier_fournisseur_gest("data/fournisseur.dat");
    break;

  case 3:
    supprimer_fournisseur_gest("data/fournisseur.dat");
    break;

  case 4:
    rechercher_fournisseur_gest("", 0, NULL, NULL, NULL, 0, "data/fournisseur.dat");
    break;

  case 5:
    afficher_fournisseur_gest("data/fournisseur.dat");
    break;
  }
}

void gerer_produits() {
  printf("\n\n=== Gerer les produits ===\n");
  printf("1. Ajouter un nouveau produit\n");
  printf("2. Modifer les informations d'un produit\n");
  printf("3. Supprimer un produit\n");
  printf("4. Rechercher un produit\n");
  printf("5. Afficher les produits\n");

  int action_gest_pr = saisie_int(1, 5, "Entrez l'action: ", bright_green, "", "");

  switch (action_gest_pr)
  {

  case 1:
    ajouter_produit_gest("data/produit.dat");
    break;

  case 2:
    modifier_produit_gest("data/produit.dat");
    break;

  case 3:
    supprimer_produit_gest("data/produit.dat");
    break;

  case 4:
    rechercher_produit_gest("", 0, NULL, NULL, NULL, 0, "data/produit.dat");
    break;

  case 5:
    afficher_produit_gest("data/produit.dat");
    break;
  }
}

void consulter_tab_bord_stock() {
  printf("\n\n=== Tableau de bord des stocks ===\n");
  printf("1. Afficher les produits disponibles\n");
  printf("2. Afficher les produits en attente de livraison\n");
  printf("3. Consulter la liste des clients\n");
  printf("4. Consulter la liste des fournisseurs\n");

  int action_gest_tab = saisie_int(1, 4, "Entrez l'action: ", bright_green, "", "");

  switch (action_gest_tab)
  {

  case 1:
    afficher_prod_dispo("data/produit.dat");
    break;

  case 2:
    afficher_prod_en_att("data/produit.dat");
    break;

  case 3:
    consulter_cl_prod("data/client.dat", "data/commande_client.dat");
    break;

  case 4:
    consulter_fournisseur_prod("data/fournisseur.dat", "data/commande_client.dat");
    break;
  }
}

int se_connecter_client(client* cl) {
  char tel[10], mdp[30];
  saisie(tel, "Donner votre numero de telephone: ", '0', '9', bright_white, "", "");
  client arrcl[100];
  int narrcl, p;
  chargerTabClient("data/client.dat", arrcl, &narrcl);
  if ((p = recherche_tel_client(arrcl, narrcl, tel)) != -1) {
    verifier_mdp("Mot de passe: ", mdp, arrcl[p].mdp, bright_white, "", "");
    *cl = arrcl[p];
    return 1;
  }
  else {
    colored_text("Le numero de telephone est incorrect, ou vous n'avez pas de compte", bright_red, "", "");
    int choix = saisie_int(1, 2, "\n\n1. Reessayer\n2. Quitter\n\nEntrez l'action: ", white, "", "");
    switch (choix)
    {
    case 1:
      return se_connecter_client(cl);
    case 2:
      exit(0);
    }
    return 0;
  }
}

int se_connecter_fournisseur(fournisseur* fo) {
  char tel[10], mdp[30];
  saisie(tel, "Donner votre numero de telephone: ", '0', '9', bright_white, "", "");
  fournisseur arrfo[100];
  int p, narrfo;
  chargerTabFournisseur("data/fournisseur.dat", arrfo, &narrfo);
  if ((p = recherche_tel_fournisseur(arrfo, narrfo, tel)) != -1) {
    verifier_mdp("Mot de passe: ", mdp, arrfo[p].mdp, bright_white, "", "");
    *fo = arrfo[p];
    return 1;
  }
  else {
    colored_text("Le numero de telephone est incorrect, ou vous n'avez pas de compte", bright_red, "", "");
    int choix = saisie_int(1, 2, "\n\n1. Reessayer\n2. Quitter\n\nEntrez l'action: ", white, "", "");
    switch (choix)
    {
    case 1:
      return se_connecter_fournisseur(fo);
    case 2:
      exit(0);
    }
    return 0;
  }

}

void menu_actions_client(client cl) {
  colored_text("\n=== Menu client ===\n", bright_yellow, "", "");
  printf("1. Acheter un produit\n");
  printf("2. Demander une facture\n");
  printf("3. Consultation mon compte\n");
  int action_cl = saisie_int(1, 3, "Entrez l'action: ", magenta, bold, "");
  printf("\n");
  switch (action_cl)
  {
  case 1:
    acheter_produit_client(cl, "data/produit.dat", "data/commande_client.dat", "data/nouveaux_noti_gest.txt");
    break;

  case 2:
    demande_facture_client(cl, "data/commande_client.dat", "data/magasin.dat");
    break;
  case 3:
    consulter_compte_client(cl, "data/commande_client.dat", "data/magasin.dat");
    break;
  }
}

void menu_actions_fournisseur(fournisseur fo) {
  colored_text("\n=== Menu fournisseur ===\n", bright_yellow, "", "");
  printf("1. Valider les commandes\n");
  printf("2. Consultation mon compte\n");
  int action_fo = saisie_int(1, 2, "Entrez l'action: ", magenta, bold, "");
  printf("\n");
  switch (action_fo)
  {
  case 1:
    validation_commandes_fournisseur(fo, "data/magasin.dat", "data/commande_gest.dat", "data/produit.dat");
    break;

  case 2:
    consulter_compte_fournisseur(fo, "data/commande_gest.dat");
    break;
  }
}