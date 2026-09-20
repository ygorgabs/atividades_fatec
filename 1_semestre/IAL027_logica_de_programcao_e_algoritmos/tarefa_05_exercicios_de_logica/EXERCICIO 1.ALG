Algoritmo "Exercicio 1"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen Lucia
// Descrição   : Calcula a area do retangulo
// Autor(a)    : Ygor Gabriel
// Data atual  : 13/09/2025
Var
   // Seção de Declarações das variáveis
   base, altura, area : inteiro
   continua : caractere
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   repita
      escreval("Digite o valor da base do retangulo: ")
      leia(base)
      escreval("Digite o valor da altura do retangulo: ")
      leia(altura)
      area <- base * altura
      escreval("A area do retangulo e: ",area)
      escreval("Deseja calcular novamente?[S/N]")
      leia(continua)
   ate maiusc(continua) <> "S"
Fimalgoritmo