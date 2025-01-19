#ifndef DISPLAY_H
#define DISPLAY_H

void colored_text(char* text, const char* color, const char* bd, const char* ud);
void remplir_table(char** tab, int* p, int n, int start, ...);
void repeter_carac(char* s, int n, char c);
void print_table(char** tab, int* length, int l, int c);

void print_client(client cl, char** tab, int* length, int start);
void print_produit(produit pr, char** tab, int* length, int start, short en_arrivage);
void print_fournisseur(fournisseur fo, char** tab, int* length, int start);
short print_magasin(char* file_name);
// void print_facture(facture fa, float tva);

void afficher_list_ordonee(char** p, int n);
void afficher_list_client(client* arr_cl, int n);
void afficher_list_fournisseur(fournisseur* arr_fo, int n);
void afficher_list_produit(produit* arr_pr, int n);

#endif