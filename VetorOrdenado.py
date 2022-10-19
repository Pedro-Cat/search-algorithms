class VetorOrdenado:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.cidades = [None] * tamanho
            
            
    def inserir(self, cidade):
        if self.numeroElementos == 0:
            self.cidades[0] = cidade
            self.numeroElementos = 1
            return
        
        posicao = 0
        while posicao < self.numeroElementos:
            if cidade.distanciaObjetivo < self.cidades[posicao].distanciaObjetivo:
                break
            posicao += 1
            
        for k in range(self.numeroElementos, posicao, -1):
            self.cidades[k] = self.cidades[k-1]
            
        self.cidades[posicao] = cidade
        self.numeroElementos += 1
        
    def getPrimeiro(self):
        return self.cidades[0]
    
    def mostrar(self):
        for i in range(self.numeroElementos):
            print(f'{self.cidades[i].nome} - {self.cidades[i].distanciaObjetivo}')


'''from Mapa import *
mapa = Mapa()
vetor = VetorOrdenado(5)
vetor.inserir(mapa.portoUniao) # 203
vetor.inserir(mapa.pauloFrontin) # 172
vetor.inserir(mapa.balsaNova) # 41
vetor.mostrar()
vetor.inserir(mapa.palmeira) # 59'''
