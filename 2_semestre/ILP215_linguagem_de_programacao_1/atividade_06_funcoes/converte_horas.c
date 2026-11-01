#include <stdio.h>
#include <locale.h>

int converterHorasEmSegundos(int hora, int min, int seg){
	return hora*3600+min*60+seg;
}

int main(){
	setlocale(LC_ALL, "Portuguese");
	int hora, min, seg;
	printf("Conversor\n");
	printf("*****************************\n");
	printf("Digite as horas, minutos e segundos separados por espaço: ");
	scanf("%d %d %d", &hora, &min, &seg);
	printf("O resultado em segundos é: %d\n",converterHorasEmSegundos(hora,min,seg));
        return 0;
}