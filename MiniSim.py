class memory:
    def __init__(self, size):
        self.partitionList = []
        self.size = size #In MB

    def add_partition(self, tamanho):
        self.tamanhoTotal = sum(self.partitionList)
        if self.tamanhoTotal == self.size:
            print("memoria completamente particionada, nao pode adicionar mais uma particao")
        elif self.tamanhoTotal + tamanho > self.size:
            self.partitionList.append(self.size - self.tamanhoTotal)
        else:
            self.partitionList.append(tamanho)
        

        


memoria = memory(100)
memoria.add_partition(20)
memoria.add_partition(40)
memoria.add_partition(10)
memoria.add_partition(30)
print("Essa eh a minha memoria particionada: ")
print(memoria.partitionList)



