
codigo = input("Digite o código do produto: ")


nome = input("Digite o nome do produto: ")


quantidade = int(input("Digite a quantidade do produto: "))


preco = float(input("Digite o preço do produto: "))


valor_total = quantidade * preco


print("\nInformações do produto cadastrado:")
print("Código:", codigo)
print("Nome:", nome)
print("Quantidade:", quantidade)
print("Preço:", preco)
print("Valor total da compra:", valor_total)
