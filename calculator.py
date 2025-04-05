#Estrutura básica de uma calculadora usando Python

#Lista para guardar as últimas operações feitas
historico = []

#Função main 
def main():
    while True:     #Estrutura de repetição para opção
        print("=" * 30)
        print("--> CALCULADORA EM PYTHON <---".center(30))
        print("=" * 30)
        print("--> 1 - SOMA")
        print("--> 2 - SUBTRAÇÃO")
        print("--> 3 - MULTIPLICAÇÃO")
        print("--> 4 - DIVISÃO")
        print("--> 5 - POTÊNCIAÇÃO")
        print("--> 6 - HISTÓRICO")
        print("--> 7 - SAIR")
    #Opção de erro, caso a opção inserida não seja um número
        try:  
            opcao = int(input("\nSelecione uma opção: "))
        except ValueError:
            print("Erro! Digite um número válido.")
            continue
    #Opção de escolha entre 1 e 7, onde cada um tem sua específica função a ser exibida e executada
        try:
            if opcao == 1:
                soma() #Função de soma
            elif opcao == 2:
                subtracao() #Função de subtração
            elif opcao == 3:
                multiplicacao() #Função de multiplicação
            elif opcao == 4:
                divisao() #Função de divisão
            elif opcao == 5:
                potencia() #Função de potenciação
            elif opcao == 6:
                ver_historico() #Função para exibir histórico
            elif opcao == 7:
                print("Saindo...") #Sair
                break
            else:
                print("Digite uma opção válida.")
        except ValueError:
            print("Erro! Digite uma opção válida.")
            continue
try:           
    def soma():
        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))
        resultadosoma = num1 + num2
        print(f"\nO resultado da soma é: {resultadosoma:.2f}")
        historico.append(f"{num1} + {num2} = {resultadosoma}") #Append para adicionar as histórico
     
    def subtracao():
        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))
        resultadosubtracao = num1 - num2
        print(f"\nO resultado da subtração é: {resultadosubtracao:.2f}")
        historico.append(f"{num1} - {num2} = {resultadosubtracao}")
        
    def multiplicacao():
        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))
        resultadomultiplicacao = num1 * num2
        print(f"\nO resultado da multiplicação é: {resultadomultiplicacao:.2f}")
        historico.append(f"{num1} * {num2} = {resultadomultiplicacao}")
          
    def divisao():
        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))
    #If para a divisão não ser divisível por 0, caso não tivesse o IF, erro ia dar na hora de ser inserido o número 0
        if num2 == 0:
            print("Erro: A divisão não pode ser por 0. Tente novamente")
            return
        
        resultadodivisao = num1 / num2
        print(f"\nO resultado da divisão é: {resultadodivisao:.2f}")
        historico.append(f"{num1} / {num2} = {resultadodivisao}")

    def potencia():
        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))
        resultadopotencia = num1 ** num2
        print(f"\nO resultado da potenciação é: {resultadopotencia:.2f}")
        historico.append(f"{num1} ** {num2} = {resultadopotencia}")
    
    def ver_historico():
        print("\n--> HISTÓRICO DE OPERAÇÃOES <--")
        if not historico: #Exibição caso nenhuma operação tenha sido executada
            print("Não há operações.")
        else:
            for i, operacao in enumerate(historico, start=1):
                print(f"{1}. {operacao}") #Adicionando a operação ao histórico com "1." e a operação em seguida
        
                
except ValueError:
    print("Error! Digite número válidos.")
    
main()
