#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

void main(){
	setlocale(LC_ALL,"");
	int voto = 0, ana = 0, bruno = 0, carlos = 0, invalido = 0, valido = 0;
	
	do{
		printf("Digite o número do candidato escolhido:\n");
		printf("1 - Ana\n2 - Bruno\n3 - Carlos\n0 - Encerrar votação\n");
		scanf("%d", &voto);
		
		
		switch(voto){
			case 0:
				break;
			case 1: 
				ana++; break;
			case 2:
				bruno++; break;
			case 3:
				carlos++; break;
			default:
				invalido++; break;
		}
		
		system("clear");		
	}while(voto != 0);
	
	valido = ana + bruno + carlos;
	printf("Votação Encerrada\n");
	printf("---------------------------------\n");
	printf("Votos:\nAna: %d votos\nBruno: %d votos\nCarlos: %d votos\n",ana,bruno,carlos);
	printf("Votos válidos: %d\nVotos inválidos: %d\n",valido,invalido);
	printf("---------------------------------\n");
	if(ana > bruno && ana > carlos){
		printf("Ana venceu a eleição\n");
	}else if(bruno > ana && bruno > carlos){
		printf("Bruno venceu a eleição\n");
	}else if(carlos > ana && carlos > bruno){
		printf("Carlos venceu a eleição\n");
	}else{
		printf("Eleição Empatada\n");
	}
}