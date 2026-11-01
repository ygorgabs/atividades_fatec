#include <stdio.h>
#include <locale.h>

void converteSegundos(int segundos){
	int horas, minutos, segundosResidual;
	horas = segundos/3600;
	minutos = (segundos%3600)/60;
	segundosResidual = (segundos%3600)%60;
	printf("%dh%dm%ds\n4", horas, minutos, segundosResidual);
}

int main(){
	setlocale(LC_ALL, "Portuguese");
	int segundos;
	
	printf("Digite o valor em segundos para converter\n");
	scanf("%d", &segundos);
	converteSegundos(segundos);
	return 0;
}