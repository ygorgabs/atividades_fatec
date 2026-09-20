Algoritmo "Exercicio 3a"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Recebe valor e mostra o proximo e o anterior
// Autor(a)    : Ygor Gabriel
// Data atual  : 18/08/2025
Var
// Seção de Declarações das variáveis 
num, ant, prox, dobroAnt, dobroProx, dobroNum : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreval("Digite um número: ")
   Leia(num)
   ant <- num - 1
   prox <- num + 1
   dobroAnt <- ant * 2
   dobroProx <- prox * 2
   dobroNum <- num * 2
   
   escreval("--------------------")
   escreval("|" , num , ant , prox , dobroNum , dobroAnt , dobroProx , "|")
   escreval("--------------------")
Fimalgoritmo