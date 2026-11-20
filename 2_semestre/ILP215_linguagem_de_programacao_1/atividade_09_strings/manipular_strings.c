#include <stdio.h>
#include <locale.h>
#include <string.h>
#include "strmod.h"
#define MAX_CHAR 40

void options(int option, char aluno[], char curso[]){
    char copia[MAX_CHAR];
    switch(option){
        case 1:
            printf("Quantidade de caracteres no nome: %zu\n", strlen(aluno)-1); 
            break;
        case 2:
            strcpy(copia,aluno);
            printf("Nome copiado: %s\n", copia);
            break;
        case 3:
            printf("Nome: %s\n",strupr(aluno));
            break;
        case 4:
            printf("Nome: %s\n",strlwr(aluno));
            break;
        case 5:
            printf("Informação concatenada: %s\n", strcat(aluno,curso));
            break;
        case 6:
            getchar();
            printf("Digite um segundo nome: ");
            fgets(copia,MAX_CHAR,stdin);
            printf("Os dois nomes são %s\n",strcmp(strupr(aluno),strupr(copia)) == 0 ? "iguais" : "diferentes");
            break;
        default:
            printf("Opção inválida\n");
    }
}

int main(){
    setlocale(LC_ALL,"");
    char aluno[MAX_CHAR], curso[MAX_CHAR];
    int op;
    printf("Digite o nome do aluno: ");
    fgets(aluno,MAX_CHAR,stdin);
    printf("Digite o nome da curso: ");
    fgets(curso,MAX_CHAR,stdin);
    printf("***********************************\n");
    printf("Escolha uma opção:\n");
    printf("1 - Qtd caracteres de aluno\n2 - Copiar nome\n3 - Exibir nome em maiúsculo\n4 - Exibir nome em minúsculo\n5 - Exibir aluno e curso\n6 - Comparar nomes\n");
    scanf("%d",&op);
    options(op, aluno, curso);
    return 0;
}