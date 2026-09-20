#include <stdio.h>
#include <locale.h>

void main(){
	setlocale(LC_ALL,"Portuguese");
	int dia, mes, ano, resultadoProvisorio,resultado;
	
	printf("Digite o dia do nascimento(DD): ");
	scanf("%d", &dia);
	
	printf("Digite o mes do nascimento(MM): ");
	scanf("%d", &mes);
	
	printf("Digite o ano do nascimento(AAAA): ");
	scanf("%d", &ano);
	
	resultadoProvisorio = dia*100+mes+ano;
	resultado = ((resultadoProvisorio % 100) + (resultadoProvisorio/100)) % 5;
	printf("O resultado foi: %d. Seu perfil é: ",resultado);
	
	switch(resultado){
		case 0: printf("Tímido\n"); break;
		case 1: printf("Sonhador\n"); break;
		case 2: printf("Paquerador\n"); break;
		case 3: printf("Atraente\n"); break;
		case 4: printf("Irresistível\n"); break;
	}
}