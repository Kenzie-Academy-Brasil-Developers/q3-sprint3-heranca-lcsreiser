# Desenvolva sua classe Recipiente aqui.


class Recipiente:
    def __init__(self, tamanho: float, conteudo=0, limpo=True):
        self.tamanho = tamanho if tamanho > 0 else 0
        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        return False

    def lavar(self):
        self.conteudo = 0
        self.limpo = True

    def esta_limpo(self):
        return self.limpo

    def estado(self):
        if self.limpo:
            return "limpo"
        else:
            return "sujo"

    def sujar(self):
        self.limpo = False

    def __str__(self):
        return f"Um recipiente {self.estado()} não especificado"

    def __repr__(self):
        return f"Um recipiente {self.estado()} não especificado"
