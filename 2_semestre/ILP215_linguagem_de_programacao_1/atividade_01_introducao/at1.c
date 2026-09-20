#include <stdio.h>
#include <locale.h>

void main(){
	int numero, dobro;
	setlocale(LC_ALL, "Portuguese");
	printf("Digite um número: ");
	scanf("%d", &numero);
	dobro = numero * 2;
	printf("O dobro de %d é: %d\n", numero, dobro);
}