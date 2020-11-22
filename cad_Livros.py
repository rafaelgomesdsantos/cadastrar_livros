#código 6 rafgds

print("-----------Cadastro de Livros----------")
inventario=[]
resposta = "S"
while resposta == "S":
    livro=[input("\nTítulo: "),
              float(input("\nValor: ")),
           (input("\nGênero: ")),]
    inventario.append(livro)
    resposta = input("\nDigite \"S\" para continuar cadastrando e \"N\" para ver os livros cadastrados: \n").upper()

for elemento in inventario:
    print("\nTítulo......: ", elemento[0])
    print("Valor.......: ", "R$", elemento[1])
    print("Gênero......:", elemento[2])
    print()