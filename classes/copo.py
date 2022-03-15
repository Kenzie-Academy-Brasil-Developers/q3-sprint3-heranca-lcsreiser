# Desenvolva sua classe Copo aqui.

from classes.recipiente import Recipiente


class Copo(Recipiente):
    # Será que preicos manter esse float e estado iniciais?
    def __init__(self, tamanho: float, conteudo=0, limpo=True):
        super().__init__(tamanho, conteudo, limpo)

    def encher(self, bebida="água"):
        if self.limpo == False:
            return "Não se pode encher um copo sujo"
        else:
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida

    def beber(self, quantidade: float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        return super().lavar()

    def __str__(self):
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"
        else:
            return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def __repr__(self):
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"
        else:
            return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"
