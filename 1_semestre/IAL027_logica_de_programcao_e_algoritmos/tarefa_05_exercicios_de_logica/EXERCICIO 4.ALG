Algoritmo "Exercicio 4"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Calcula a area do trinagulo
// Autor(a)    : Ygor Gabriel
// Data atual  : 14/09/2025
Var
   // Seção de Declarações das variáveis
   base, altura, area : real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreval("Calcule a area de um triangulo")
   Escreval("------------------------------")
   Escreva("Digite o valor da base: ")
   Leia(base)
   Escreval()
   Escreva("Digite o valor da altura: ")
   Leia(altura)
   Escreval()
   area <- (base * altura)/2
   Escreva("Area do triangulo: ",area)
Fimalgoritmo