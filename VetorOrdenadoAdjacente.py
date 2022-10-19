class VetorOrdenadoAdjacente:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.adjacentes = [None] * tamanho
            
            
    def inserir(self, adjacente):
        if self.numeroElementos == 0:
            self.adjacentes[0] = adjacente
            self.numeroElementos = 1
            return
        
        posicao = 0
        while posicao < self.numeroElementos:
            if adjacente.distanciaAEstrela < self.adjacentes[posicao].distanciaAEstrela:
                break
            posicao += 1
            
        for k in range(self.numeroElementos, posicao, -1):
            self.adjacentes[k] = self.adjacentes[k-1]
            
        self.adjacentes[posicao] = adjacente
        self.numeroElementos += 1
        
    def getPrimeiro(self):
        return self.adjacentes[0].cidade
    
    def mostrar(self):
        for i in range(self.numeroElementos):
            print(f'{self.adjacentes[i].cidade.nome} - {self.adjacentes[i].distanciaAEstrela}')

