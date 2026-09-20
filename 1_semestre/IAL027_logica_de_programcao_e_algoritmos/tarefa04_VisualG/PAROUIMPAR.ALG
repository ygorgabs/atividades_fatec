Algoritmo "ParOuImpar"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Verifica se numero e par ou impar
// Autor(a)    : Ygor Gabriel
// Data atual  : 26/08/2025
Var
   // Seção de Declarações das variáveis
   num: inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreval("Digite um número: ")
   Leia(num)
   Se num % 2 = 0 Entao
      Escreva(num, " é número par")
   Senao
      Escreva(num, " é número impar")
   Fimse
Fimalgoritmo