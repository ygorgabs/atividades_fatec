#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL,"");
    int idade;
    printf("Digite a idade do competidor: ");
    scanf("%d",&idade);

    if(idade < 13){
        printf("Categoria Infantil\n");
    }else if(idade < 18){
        printf("Categoria Juvenil\n");
    }else if(idade < 60){
        printf("Categoria Adulto\n");
    }else{
        printf("Categoria Sênior\n");
    }
}