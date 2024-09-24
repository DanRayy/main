from funcoes import ManipularTextos

class Texto:
    def __init__(self, escolha) -> None:
        self.escolha = escolha

    def chamar_escolha(self):
        manipular = ManipularTextos('texto')
        manipular.escrever_texto()

        print("1 - Inverter textos\n2 - Contar caracteres\n3 - Substituir um caractere")
        self.escolha = input("Escolha uma opção: ")

        match self.escolha:
            case '1':
                manipular.inverter_texto()
            case '2':
                manipular.contar_caracteres()
            case '3':
                manipular.substituir_caractere()
            case _:
                print("Escolha uma opção válida!")

texto = Texto('texto')
texto.chamar_escolha()
