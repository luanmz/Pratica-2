import random
import math

class Memoria():
    def __init__(self, tamanho, pagesize):
        self.tamanhoPrincipal = tamanho
        self.tamanhoVirtual = 2*tamanho
        self.pagesize = pagesize
        self.pagelist = []
        self.pagelistP = []
        self.swap = []
        for x in range (int(self.tamanhoVirtual/pagesize)): #tamanho e pagesize precisam ser múltiplos de 2
            self.pagelist.append(Pagina((x+1), pagesize))

    def add_processo(self, processo):
        print(f"{processo.nome} tem {processo.processSize} MBs\n")
        tamanho = processo.processSize
        counter = 0 
        memoriaLivre = 0

        for x in self.pagelist:
            if x.status == "Livre":
                 memoriaLivre += x.size

        while tamanho > 0 and counter < len(self.pagelist):
           
           
            if tamanho > memoriaLivre:
                print(f"{processo.nome} nao pode ser alocado na memoria virtual!\n")
                break
            
            if self.pagelist[counter].status == "Livre":
                processo.alocation.append(self.pagelist[counter])
                tamanho -= self.pagelist[counter].size
                print(f"{processo.nome} ocupou a pagina {self.pagelist[counter].id}\n")
                self.pagelist[counter].status = "Ocupado"
                if tamanho < 0:
                    print(f"Houve fragmentacao interna de {abs(tamanho)} MBs  na pagina {self.pagelist[counter].id}\n")
                else:
                    print(f"Nao houve fragmentacao interna na pagina {self.pagelist[counter].id}\n")
            counter += 1
        
        
        if processo.alocation != []:
            print(f"{processo.nome} esta nas paginas:")
            print([x.id for x in i.alocation])
            print(f"\nAlocando Paginas do {processo.nome}\n")
            self.fifo(processo) #Aloca o processo na fisica


    def fifo(self, processo):
        if sum([x.size for x in self.pagelistP]) + sum([x.size for x in processo.alocation]) < self.tamanhoPrincipal:
            self.pagelistP.extend(processo.alocation)
            for x in processo.alocation:
                print(f"Pagina {x.id} esta na memoria principal\n")
        else:
            # numpag = math.ceil(processo.processSize/self.pagesize)
            # print(numpag)
            # for i in range(numpag):
            #     print(f"\nPagina {self.pagelistP[i].id} esta saindo da memoria principal")
            #     self.swap.append(self.pagelistP.pop(i))
            # self.fifo(processo)

            print(f"{processo.nome} nao pode ser alocado na memoria principal\n")
            
               


            


class Pagina():
    def __init__(self, _id, size):
        self.id = _id
        self.size = size
        self.status = "Livre"
        self.referencia = 0


class Processo():
    def __init__(self, nome, ID, processSize):
        self.nome = nome
        self.ID = ID
        self.processSize = processSize
        self.alocation = []


#Trecho de código onde eu crio meus processos automaticamente recebendo apenas a quantidade:
def listaProcesso(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(Processo(f"Processo {i+1}", i+1, random.randint(8,12)))
    return lista
        


#Na instanciação da memória voce define o tamanho da memória principal (memoria virtual automaticamente atualizada com 2x o tamanho da principal) e o tamanho das páginas:
memoria = Memoria(16, 4) 

#Chamo a função que cria as listas
lista = listaProcesso(4)

#Adiciono cada processo da lista a minha memória virtual e posteriormente na fisica:
for i in lista:
    memoria.add_processo(i)
    

#Aqui apenas printamos o status de cada pagina na minha memória virtual:
print("Status das minha paginas virtuais:\n")
for x in memoria.pagelist:
    print(f"status da pagina {x.id} eh:",x.status)