programa {
  funcao inicio() {
    caracter operador
    real resultado = 0.0, N1, N2
    inteiro continuar
 
    escreva("Digite o primeiro número: ")
    leia(N1)
 
    escreva("Digite o segundo número: ")
    leia(N2)
 
    escreva("\n")
   
    escreva("Agora digite uma das operações (+ - * /): ")
    leia(operador)
 
    se (operador == '+') {
      resultado = N1 + N2
    }
    senao se (operador == '-') {
      resultado = N1 - N2
    }

    	senao se(operador == '/')
		{
			resultado = N1 / N2
			
		}
		senao se(operador == '*')
		{
			resultado = N1 * N2
		}	
 
    limpa()
   
    escreva("Resultado:\n\n")
    escreva(N1, " ", operador, " ", N2, " = ", resultado)
   
    escreva("\n")
   
    escreva("\nDeseja continuar na calculadora?\n")
    escreva("1 - Sim\n")
    escreva("2 - Não\n")
 
    escreva("\nDigite a opção desejada: ")
    leia(continuar)
 
    se (continuar == 2) {
      escreva("Calculadora fechada.")
    }
  }
}
 