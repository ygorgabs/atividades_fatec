Algoritmo "Exercicio 2"
// Disciplina   : [Algoritimos e Lógica de Programação]
// Professor   : Carmen Lucia
// Descrição   : Calcula reajuste de salario
// Autor(a)    : Ygor Gabriel
// Data atual  : 13/09/2025
Var
   // Seção de Declarações das variáveis
   i, dependente, cont10, cont12 : inteiro
   salario: vetor[1..2] de real
   nome: vetor[1..2] de caractere
   continua: caractere

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   continua <- "S"
   cont10 <- 0
   cont12 <- 0

   repita
      para i de 1 ate 2 faca
         escreval("Digite o nome do ",i,". funcionario: ")
         leia(nome[i])
         escreval("Digite o salario do ",i,". funcionario: ")
         leia(salario[i])
         
         se salario[i] > 3500 entao
            salario[i] <- salario[i]*1.1
            cont10 <- cont10 + 1
         senao
             salario[i] <- salario[i]*1.12
             cont12 <- cont12 + 1
         fimse
         
         escreval("Digite o numero de dependentes do funcionario: ")
         leia(dependente)
         
         se dependente > 0 entao
            salario[i] <- salario[i] + (dependente * 250)
         fimse
      fimpara
      
      para i de 1 ate 2 faca
           escreval("Funcionario ",nome[i]," - Salario ajustado: R$",salario[i])
      fimpara
      
      escreval("Deseja calcular reajuste para outros funcionarios? [S/N]")
      leia(continua)
   ate maiusc(continua)<> "S"
   
   escreval("Total de funcionarios com reajuste de 10%: ", cont10)
   escreval("Total de funcionarios com reajuste de 12%: ", cont12)

Fimalgoritmo