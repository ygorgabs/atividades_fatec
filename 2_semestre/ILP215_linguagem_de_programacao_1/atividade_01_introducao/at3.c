#include <stdio.h>
#include <locale.h>

void main(){
	float valorUnit, valorVenda;
	int qtd;
	
	setlocale(LC_ALL, "Portuguese");
	
	printf("Digite o valor unitário: ");
	scanf("%f", &valorUnit);
	printf("Digite a quantidade vendida: ");
	scanf("%d", &qtd);
	valorVenda = valorUnit * qtd;
	printf("A soma é: %.2f\n",valorVenda);
}