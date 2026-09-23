#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL,"");
    float salario, bonus;
    int tempo_empresa;

    printf("Digite o salário do funcionário: ");
    scanf("%f", &salario);
    printf("Digite o tempo de trabalho em anos: ");
    scanf("%d",&tempo_empresa);
    printf("Salario: R$%.2f\n",salario);
    if(tempo_empresa < 2){
        bonus = 0.0;
    }else if(tempo_empresa <= 5){
        bonus = salario * 0.05;
    }else if(tempo_empresa <= 10){
        bonus = salario * 0.1;
    }else{
        bonus = salario * 0.15;
    }
    printf("Bonus: R$ %.2f\nTotal a receber: R$%.2f\n",bonus, salario + bonus);
}