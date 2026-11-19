#include <stdio.h>
#include <locale.h>

int potenciacao(int base, int expoente){
	if (expoente == 0) return 1;
	else return base * potenciacao(base, expoente-1);
}

int main(){
	int base, expoente;
	setlocale(LC_ALL,"");
	printf("Calcular de potenciação\n");
	printf("***********************\n");
	printf("Digite o valor da base: ");
	scanf("%d",&base);
	printf("Digite o valor do expoente: ");
	scanf("%d",&expoente);
	printf("\nResultado: %d\n",potenciacao(base,expoente));
	return 0;
}