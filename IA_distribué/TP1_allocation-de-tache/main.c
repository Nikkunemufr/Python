#include <stdio.h>
#include <stdlib.h>

//Calcul la somme de collectivité et la retourne
int compute_SWutilitarian(int **collectivity, size_t size) {
  int utilitarian = 0;
  for (int i = 0; i < size; i++) {
    utilitarian += collectivity[i];
  }
  return utilitarian;
}

//Calcul le minimum de la collectivité et le retourne
int compute_SWEgalitarianism(int **collectivity, size_t size) {
  int egalitarianism = 2147483647; //Max integer value in 32 bit unsigned int
  for (int i = 0; i < size; i++) {
    if (egalitarianism > collectivity[i]) {
      egalitarianism = collectivity[i];
    }
  }
  return egalitarianism;
}

//Calcul le maximum de la collectivité et le retourne
int compute_SWElitist(int **collectivity, size_t size) {
  int elitist = 0;
  for (int i = 0; i < size; i++) {
    if (elitist < collectivity[i]) {
      elitist = collectivity[i];
    }
  }
  return elitist;
}

//Calcul le produit de la collectivité et le retourne
int compute_SWNashProduct(int **collectivity, size_t size) {
  int nashProduct = 1;
  for (int i = 0; i < size; i++) {
    nashProduct *= collectivity[i];
  }
  return nashProduct;
}

//Donne la priorité la plus haute de la population en utilisant la méthode indiqué via le SWcode
int compare(int *population, size_t size, size_t nbAgent, int SWcode) { // int ** population == int population[][]
  int collectivity = 0;
  for (int i = 0; i < size; i++) {
    int tampon = 0;
    int * subArray[nbAgent];
    for (int j = 0; j < nbAgent; j++) {
      subArray[j] = population[i+j];
    }
    switch(SWcode) {
      case 0 :
        tampon = compute_SWutilitarian(subArray, nbAgent);
        break;
      case 1 :
        tampon = compute_SWEgalitarianism(subArray, nbAgent);
        break;
      case 2 :
        tampon = compute_SWElitist(subArray, nbAgent);
        break;
      case 4 :
        tampon = compute_SWNashProduct(subArray, nbAgent);
        break;
      default :
        printf("Error ! the SW code is not correct");
     }
     if (collectivity < tampon) {
       collectivity = tampon;
     }
  }
  return collectivity;
}

void main () {
  size_t nbAgent = 4;
  size_t size = 3;
  int U[] = {19,3,5,2};
  int population[] = {19,3,5,2,9,9,9,9,5,71,54,2};
  printf("utilitarian : %d \n", compute_SWutilitarian(U, nbAgent));
  printf("egalitarianism : %d \n", compute_SWEgalitarianism(U, nbAgent));
  printf("elitist : %d \n", compute_SWElitist(U, nbAgent));
  printf("nashProduct : %d \n", compute_SWNashProduct(U, nbAgent));
  printf("compare : %d \n", compare(population, size, nbAgent, 0));

}
