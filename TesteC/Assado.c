#include <stdio.h>

int main(void) {
//declaração de variável
  float nota1, nota2, media;
  

  //Capturar as notas que o usuário digita
  printf("Digite a primeira nota: ");
  scanf("%f", &nota1);

  printf("Digite a segunda nota: ");
  scanf("%f", &nota2);
  //Calcular a média
  media = (nota1 + nota2)/2;
  
  
  //verificar se o aluno foi aprovado ou não
  if(media >= 7)
    printf("Aprovado sua nota foi %f", media);
  else
    printf("Reprovado sua nota foi %f", media) ;
  
  

  return 0;
}