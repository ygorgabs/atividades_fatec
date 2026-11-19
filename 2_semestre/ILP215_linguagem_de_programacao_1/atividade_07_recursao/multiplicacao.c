#include <stdio.h>
#include <locale.h>

int multiplicacao(int fator1, int fator2){
	if(fator2 == 0) return 0;
	else return fator1 + multiplicacao(fator1, fator2 - 1);
}

int main(){
	int fator1, fator2;
	setlocale(LC_ALL,"");
	printf("Calcular de multiplicacao\n");
	printf("***********************\n");
	printf("Digite o valor do fator 1: ");
	scanf("%d",&fator1);
	printf("Digite o valor do fator 2: ");
	scanf("%d",&fator2);
	printf("\nResultado: %d\n",multiplicacao(fator1, fator2));
	return 0;
}