class ManipularTextos:
    def __init__(self, texto) -> None:
        self.texto = texto

    def escrever_texto(self):
        self.texto = input("\033[32mDigite um texto: \033[m")

    def inverter_texto(self):
        texto_invertido = self.texto[::-1] 
        print(f"\033[31mTexto invertido: \033[m{texto_invertido}")

    def contar_caracteres(self):
        caracteres = len(self.texto)
        print(f"Existem \033[36m{caracteres}\033[m caracteres em seu texto! ")

    def substituir_caractere(self):
        while True:
            
            subst = input("Digite apenas 1 caractere: ")
            verif = len(subst)
            if verif != 1:
                print("Digite apenas 1 caractere! ")

            else:
                subst_char = input("Qual caractere do seu texto você quer substituir? ")
                print(self.texto.replace(subst_char, subst))
            break

ManipularTextos('texto')
