#include <stdio.h>
#include <locale.h>

void main(){
	float num1, num2, soma;
	setlocale(LC_ALL, "Portuguese");
	printf("Digite o primeiro valor: ");
	scanf("%f", &num1);
	printf("Digite o segundo valor: ");
	scanf("%f", &num2);
	soma = num1 + num2;
	printf("A soma é: %.2f\n",soma);
}