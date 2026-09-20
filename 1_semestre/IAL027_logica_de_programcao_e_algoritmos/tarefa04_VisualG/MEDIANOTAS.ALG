Algoritmo "MediaNotas"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Calcula media de notas
// Autor(a)    : Ygor Gabriel
// Data atual  : 26/08/2025
Var
   // Seção de Declarações das variáveis
   nota1, nota2, nota3, media : real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreval("Digite a primeira nota: ")
   leia(nota1)
   escreval("Digite a segunda nota: ")
   leia(nota2)
   escreval("Digite a terceira nota: ")
   leia(nota3)
   media <- (nota1 + nota2 + nota3) / 3
   escreval("A média é: ", media)
Fimalgoritmo