Algoritmo "Exercicio 3"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen Lucia
// Descrição   : verifica se um valor e par ou impar
// Autor(a)    : Ygor Gabriel
Var
// Seção de Declarações das variáveis 
i,num, cont,contPar: inteiro
pares:vetor[1..10] de inteiro
resposta:caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
cont <- 0
contPar <- 0
resposta <- "S"

repita
   cont <- cont + 1
   escreval("Digite um numero para saber se é par ou impar: ")
   leia(num)
   
   se num % 2 = 0 entao
      escreval("O número é par")
      contPar <- contPar + 1
      pares[contPar] <- num
   senao
      escreval("O número é impar")
   fimse
   
   escreval("Deseja verificar outro numero? ")
   leia(resposta)
ate (cont > 10) ou (maiusc(resposta) <> "S")

escreval("Total de numeros pares digitados: ",contPar)
para i de 1 ate contPar faca
    escreva(pares[i]," ")
fimpara

Fimalgoritmo