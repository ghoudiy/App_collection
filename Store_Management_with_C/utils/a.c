// #include <stdio.h>
// #include <stdlib.h>
// #include <limits.h>
// int main() {

//   typedef struct
//   {
//     unsigned int jj, mm, an;
//   } date;

//   typedef struct
//   {
//     char nom[30], prenom[30], tel[10], adresse[50], email[30], pays[30], fonction[30], societe[30], mdp[30];
//     date dn;
//   } client;

//   FILE* file = fopen("../data/client.dat", "wb");
//   if (file == NULL) {
//     printf("Hello");
//     return 1;
//   }
//   client cl;
//   cl.dn.an = 2005;
//   cl.dn.an = 10;
//   cl.dn.an = 7;
//   fwrite(&cl, sizeof(client), 1, file);
//   fclose(file);

//   return 0;
// }