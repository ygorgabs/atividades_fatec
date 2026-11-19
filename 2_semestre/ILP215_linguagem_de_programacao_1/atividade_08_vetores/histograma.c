#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#define SIZE 7

void histograma(int temperatures[]){
    char daysWeek[] = {'S','T','Q','Q','S','S','D'};
    for (int i = 0; i < SIZE; i++){
        printf("%c: ",daysWeek[i]);
        for(int j = 0; j <= temperatures[i]; j++){
            printf("*");
        }
        printf("\n");
    }
}

int main(){
    setlocale(LC_ALL,"");
    
    int temperatureDays[SIZE];
    printf("Digite a temperatura para os dias da semana em graus celsius\n");
    printf("**************************************************************\n");
    for(int i = 0; i < SIZE; i++){
        printf("Dia %d: ",i+1);
        scanf("%d",&temperatureDays[i]);
    }
    system("clear");
    histograma(temperatureDays);
    return 0;
}