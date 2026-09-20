#include <stdio.h>
#include <locale.h>

void main(){
	setlocale(LC_ALL,"Portuguese");
	char sexo;
	float altura, pesoIdeal;
	
	printf("Digite seu sexo (M/F): ");
	scanf("%c", &sexo);
	
	if(sexo == 'M' || sexo == 'F'){
		printf("Digite sua altura: ");
		scanf("%f", &altura);

		switch(sexo){
			case 'M': pesoIdeal = (72.7 * altura) - 58; break;
			case 'F': pesoIdeal = (62.1 * altura) - 44.7; break;
		}
		printf("Seu peso ideal é: %.2f\n",pesoIdeal);
	}else{
		printf("Para sexo digitar somente M ou F.");
	}
}