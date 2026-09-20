Algoritmo "Exercicio 5"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Converte temperatura
// Autor(a)    : Ygor Gabriel
// Data atual  : 14/09/2025
Var
// Seção de Declarações das variáveis 
 C, F, K : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

Escreval("Conversor de temperatura")
Escreval("------------------------")
Escreva("Digite a temperatura em ºC: ")
Leia(C)
K <- C + 273.15
Escreval(K, " K")
F <- (C * (9/5))+32
Escreval(F, " ºF")
Escreval()
Escreval()
Escreval()
Escreval("---------------------")
Escreval(C,"ºC = ", K, "K = ",F,"ºF")

Fimalgoritmo