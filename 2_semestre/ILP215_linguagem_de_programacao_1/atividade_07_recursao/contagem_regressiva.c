#include <stdio.h>
#include <locale.h>

void regressao(int num){
	printf("%d ", num);
	if(num > 1) regressao(num - 1);
}

int main(){
	int num;
	setlocale(LC_ALL,"Portuguese");
	printf("Imprimir a contagem regressiva a patir de qual número: ");
	scanf("%d",&num);
	printf("********************************************************\n");
	regressao(num);
    printf("\n");
	return 0;
}