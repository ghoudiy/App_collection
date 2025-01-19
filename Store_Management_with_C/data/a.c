#include<stdio.h>
#include"../utils/declaration.h"

int main() {
  //   FILE *file = fopen("gestionnaire.dat", "rb");
  // //  FILE *file = fopen("gestionnaire.dat", "rb");
  // //  fprintf(file, "newpassword");  
  // char mdp[30];
  //   fgets(mdp, sizeof(mdp), file);
  //   printf("Password: '%s'", mdp);
  // fclose(file);

  FILE* file;
  // file = fopen("commande_client.dat", "ab");
  // fwrite(&client1, sizeof(commande_client), 1, file);
  // fclose(file);

  file = fopen("commande_client.dat", "rb");
  if (file == NULL) {
    printf("null");
  }
  else
    printf("Not null");
  commande_client comnd_cl;
  while (fread(&comnd_cl, sizeof(commande_client), 1, file) == 1) {
    printf("Hello, %s, %s, %s, %s, %s, %s\n", comnd_cl.id, comnd_cl.tel, comnd_cl.nom, comnd_cl.prenom, comnd_cl.descrp, comnd_cl.marque);
    printf("%d, %f, %f, %d/%d/%d, %d/%d/%d\n", comnd_cl.qt, comnd_cl.pau, comnd_cl.tva, comnd_cl.dach.an, comnd_cl.dach.mm, comnd_cl.dach.jj, comnd_cl.dliv.an, comnd_cl.dliv.mm, comnd_cl.dliv.jj);
  }
  fclose(file);
}
