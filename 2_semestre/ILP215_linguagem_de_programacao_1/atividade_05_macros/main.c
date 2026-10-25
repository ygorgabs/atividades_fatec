#include <stdio.h>
#include <locale.h>
#include "operacoes.h"

void main(){
	setlocale(LC_ALL, "");
	
	int num1 = 0, num2 = 0, op = 0, resultado = 0;
	
	printf("Digite o primeiro valor: ");
	scanf("%d", &num1);
	printf("\nDigite o segundo valor: ");
	scanf("%d", &num2);
	
	printf("\nEscolha a operação a ser realizada:\n1 - soma\n2 - subtração\n3 - multiplicacao\n4 - maior numero\n");
	scanf("%d",&op);
	
	switch(op){
		case 1:
			resultado = somar(num1,num2); break;
		case 2:
			resultado = subtrair(num1,num2); break;
		case 3:
			resultado = multiplicar(num1,num2);break;
		case 4:
			resultado = maior(num1,num2);break;
		default:
			printf("\nOperação inválida\n");return;
	}
	
	printf("\nResultado: %d\n", resultado);
}