#include <stdio.h>
#include "declaration.h"

long unsigned int
size_cl = sizeof(client),
size_mag = sizeof(magasin),
size_prod = sizeof(produit),
size_fact = sizeof(facture),
size_fo = sizeof(fournisseur),
size_comnd_cl = sizeof(commande_client),
size_comnd_gest = sizeof(commande_gest);

char* informations[9] = { "Nom", "Prenom", "Tel", "Email", "Adresse", "Pays", "Fonction", "Societe", "Mot de passe" };
char* magasin_informations[5] = { "Nom", "Adresse", "Fax", "Tel", "Timbre" };
char* produit_informations[7] = { "ID", "Quantité", "Description", "Marque", "PAU", "PVU", "TVA" };
char* facture_informations[7] = { "Numéro", "Quantité", "Magasin", "Date", "Produit", "Prix Unitaire", "Prix Total" };

// Define ANSI codes for text styles and colors
const char* bold = ";1";
const char* underlined = ";4";

// Define standard foreground (text) colors
const char* red = "31";
const char* green = "32";
const char* yellow = "33";
const char* blue = "34";
const char* magenta = "35";
const char* cyan = "36";
const char* white = "37";
const char* bright_red = "91";
const char* bright_green = "92";
const char* bright_yellow = "93";
const char* bright_blue = "94";
const char* bright_magenta = "95";
const char* bright_cyan = "96";
const char* bright_white = "97";
