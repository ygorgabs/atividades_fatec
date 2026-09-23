#include <stdio.h>
#include <locale.h>

void main()
{
    setlocale(LC_ALL, "");
    float num1, num2, resultado;
    bool op_valida = true;
    int operador;

    printf("CALCULADORA\n----------------------------------\n");
    printf("Digite o 1° número: ");
    scanf("%f", &num1);
    printf("Digite o 2° número: ");
    scanf("%f", &num2);
    printf("Selecione o operador:\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n");
    scanf("%d", &operador);

    switch (operador)
    {
    case 1:
        resultado = num1 + num2;
        break;
    case 2:
        resultado = num1 - num2;
        break;
    case 3:
        resultado = num1 * num2;
        break;
    case 4:
        if (num2 != 0)
        {
            resultado = num1 / num2;
        }
        else
        {
            op_valida = false;
        }
        break;
    default:
        op_valida = false;
        break;
    }

    if (!op_valida && operador == 4)
    {
        printf("Não é possível dividir por 0\n");
    }
    else if (!op_valida && operador != 4)
    {
        printf("Operador inválido\n");
    }
    else
    {
        printf("O resultado é: %f\n", resultado);
    }
}