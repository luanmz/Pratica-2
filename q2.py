import random

class Memoria():
    def __init__(self, tamanho, pagesize):
        self.tamanhoFisica = tamanho
        self.tamanhoVirtual = 2*tamanho
        self.pagelist = []
        for x in range (int(self.tamanhoVirtual/pagesize)): #tamanho e pageize precisam ser multiplos de 2
            self.pagelist.append(Pagina((x+1), pagesize))

    def add_processo(self, processo):
        print(f"{processo.nome} tem {processo.processSize} MBs")
        tamanho = processo.processSize
        counter = 0
        while tamanho > 0 and counter < len(self.pagelist):
            if self.pagelist[counter].status == "Livre":
                tamanho -= self.pagelist[counter].size
                print(f"{processo.nome} ocupou a pagina {self.pagelist[counter].id}")
                self.pagelist[counter].status = "Ocupado"
                self.pagelist[counter].referencia += 1
                if tamanho < 0:
                    print(f"Houve fragmentacao interna de {abs(tamanho)} MBs  na pagina {self.pagelist[counter].id}")
                else:
                    print(f"Nao houve fragmentacao interna na pagina {self.pagelist[counter].id}")
            counter += 1

        if tamanho > 0:
            print(f"{processo.nome} nao pode ser alocado completamente!")


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

def listaProcesso(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(Processo(f"Processo {i+1}", i+1, random.randint(8,12)))
    return lista
        



memoria = Memoria(16, 4)
lista = listaProcesso(3)
for i in lista:
    memoria.add_processo(i)
for x in memoria.pagelist:
    print(f"status da pagina {x.id} eh:",x.status)
