class Memory():
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
    
    def bf(self, id, nome, procSize):
        if sum(self.partitionList) < self.size:
            raise ValueError("Memoria nao particionada completamente! Tente novamente")
        i = 0
        print(f"\n{nome} esta sendo alocado")
        intFrag = 999999999
        index = 0
        for x in self.partitionList:
            if (x - procSize) < intFrag and (x - procSize) >= 0 and self.partitionVaga[i] == "Livre":
                intFrag = (x - procSize)
                index = i
            i += 1
        if intFrag == 999999999:
            print(f"\n{nome} nao pode ser alocado\n")
        elif self.partitionList[index] - procSize != 0:
            self.partitionVaga[index] = (id, nome , procSize)
            print(f"\n{nome} foi alocado na particao {index + 1}\n")
            print(f"\nHouve fragmentacao interna de {self.partitionList[index] - procSize} MBs para a particao {index + 1}\n")
        else:
            self.partitionVaga[index] = (id, nome , procSize) 
            print(f"\n{nome} foi alocado na particao {index + 1}")
            print(f"\nNao houve fragmentacao interna para a particao {index + 1}\n")
           
        print("Estado atual das minhas particoes: \n")
        print(self.partitionVaga)
            
            

#Aqui na instanciacao da memoria voce pode definir o seu tamanho.
memoria = Memory(100)
memoria.add_partition(20)
memoria.add_partition(40)
memoria.add_partition(10)
memoria.add_partition(30)
print("\nEssa eh a minha memoria particionada: ")
print(memoria.partitionList)
memoria.bf(1, "processo 1", 30) #best fit
memoria.bf(2, "processo 2", 25)
memoria.bf(2, "Processo 3", 50)