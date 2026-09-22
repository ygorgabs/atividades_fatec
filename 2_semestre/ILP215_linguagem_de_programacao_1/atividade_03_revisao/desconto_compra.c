#include <stdio.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");

    float valor_original, valor_desconto;
    printf("Digite o valor da compra: ");
    scanf("%f", &valor_original);
    printf("Valor a pagar: R$%.2f\n", valor_original);
    if(valor_original > 500){
        valor_desconto = valor_original - valor_original * 0.1;
        printf("Valor a pagar (desconto 10%): R$%.2f\n",valor_desconto);
    }
}