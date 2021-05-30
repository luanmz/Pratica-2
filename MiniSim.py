class memory():
    def __init__(self, size):
        self.partitionList = []
        self.partitionVaga = []
        self.size = size #In MB

    def add_partition(self, tamanho):
        tamanhoTotal = sum(self.partitionList)
        if tamanhoTotal == self.size:
            print("memoria completamente particionada, nao pode adicionar mais uma particao")
        elif tamanhoTotal + tamanho > self.size:
            print("Tamanho da particao eh grande demais, sera criada uma particao com o maior tamanho possivel.")
            self.partitionList.append(self.size - tamanhoTotal)
            self.partitionVaga.append("Livre")
        else:
            self.partitionList.append(tamanho)
            self.partitionVaga.append("Livre")
    
    def BF(self, id, nome, procSize):
        if sum(self.partitionList) < self.size:
            raise ValueError("Memoria nao particionada completamente! Tente novamente")
        i = 0
        intFrag = 999999999
        index = 0
        for x in self.partitionList:
            if (x - procSize) < intFrag and (x - procSize) >= 0 and self.partitionVaga[i] == "Livre":
                intFrag = (x - procSize)
                index = i
            i += 1
        if intFrag == 999999999:
            print(f"\n{nome} nao pode ser alocado")
        elif self.partitionList[index] - procSize != 0:
            self.partitionVaga[index] = (id, nome , procSize)
            print(f"\nHouve fragmentacao interna de {self.partitionList[index] - procSize} MBs para a particao {index + 1}")
        else:
            self.partitionVaga[index] = (id, nome , procSize)
            print(f"\nNao houve fragmentacao interna para a particao {index + 1}")
            
            

#Aqui na instanciacao da memoria voce pode definir o seu tamanho.
memoria = memory(100)
memoria.add_partition(20)
memoria.add_partition(40)
memoria.add_partition(10)
memoria.add_partition(30)
print("\nEssa eh a minha memoria particionada: ")
print(memoria.partitionList)
memoria.BF(1, "processo 1", 30)
memoria.BF(2, "processo 2", 25)
memoria.BF(2, "Processo 3", 50)
print("\n", memoria.partitionVaga)
