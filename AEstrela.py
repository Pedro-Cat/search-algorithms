from VetorOrdenadoAdjacente import *

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print(f'\nAtual: {atual.nome}')
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                AEstrela.buscar(self, self.fronteira.getPrimeiro())
    

from Mapa import *
mapa = Mapa()
ae = AEstrela(mapa.curitiba)
ae.buscar(mapa.portoUniao)
