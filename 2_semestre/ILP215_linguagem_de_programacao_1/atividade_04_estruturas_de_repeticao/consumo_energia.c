#include <stdio.h>
#include <locale.h>

void main(){
	setlocale(LC_ALL,"");
	int i, maior = 0, alto = 0, consumo = 0, soma = 0;
	float media;
	for(i = 0; i < 8; i++){
		printf("Digite o consumo de energia do setor %d em KWh: ",i+1);
		scanf("%d", &consumo);
		
		soma += consumo;
		if(consumo > 1000){
			alto++;
			printf("Setor %d - Classificação: Alto\n",i+1);
		} else if (consumo > 500){
			printf("Setor %d - Classificação: Moderado\n",i+1);
		}else{
			printf("Setor %d - Classificação: Baixo\n",i+1);
		}
		
		 
		if (consumo > maior) maior = consumo;
	}
	
	media = soma / i;
	printf("---------------------------------\n");
	printf("Maior consumo registrado: %d\n",maior);
	printf("Qtd setores com alto consumo: %d\n",alto);
	printf("Consumo médio dos setores: %.2f KWh\n",media);
}
