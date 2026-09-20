Algoritmo "ParOuImparContinua"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen
// Descrição   : Verifica se numero e par ou impar
// Autor(a)    : Ygor Gabriel
// Data atual  : 26/08/2025
Var
   // Seção de Declarações das variáveis
   num, i, qtd : inteiro
   pares : vetor[1..100] de inteiro
   op : caractere

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   qtd <- 0
   op <- "S"
   Repita
      Escreval("Digite um numero: ")
      Leia(num)

      Se num % 2 = 0 entao
         Escreval(num, " é numero par")
         qtd <- qtd + 1
         pares[qtd] <- num
      Senao
         Escreval(num, " é numero impar")
      Fimse

      Escreval("Deseja continuar? (S/N)")
      Leia(op)
   Ate maiusc(op) <> "S"

   Escreval("Numeros pares digitados")
   Escreval("------------------------")

   Para i de 1 ate qtd faca
      Escreval(pares[i])
   Fimpara

Fimalgoritmo