#include <stdio.h>
#include <locale.h>

int fatorial(int num){
	int resultado = num;
	for(int i = num-1; i > 0; i--){
		resultado *= i;
	}
	return resultado;
}

float combinacaoSimples (int n, int p){
	return fatorial(n)/(fatorial(p)*fatorial(n-p));
}

int main(){
	setlocale(LC_ALL, "");
	int n, p;
	
	printf("Digite os valores para calcular a combinação simples\n");
	printf("Valor 1: ");
	scanf("%d",&n);
	printf("Valor 2: ");
	scanf("%d",&p);
	printf("A quantidade combinações possíveis é: %.2f\n",combinacaoSimples(n,p));
	return 0;
}