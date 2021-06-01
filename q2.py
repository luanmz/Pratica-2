import random

class Memoria():
    def __init__(self, tamanho, pagesize):
        self.tamanhoFisica = tamanho
        self.tamanhoVirtual = 2*tamanho
        self.pagelist = []
        for x in range (int(self.tamanhoVirtual/pagesize)): #tamanho e pagesize precisam ser múltiplos de 2
            self.pagelist.append(Pagina((x+1), pagesize))

    def add_processo(self, processo):
        print(f"{processo.nome} tem {processo.processSize} MBs")
        tamanho = processo.processSize
        counter = 0 
        memoriaLivre = 0

        for x in self.pagelist:
            if x.status == "Livre":
                 memoriaLivre += x.size

        while tamanho > 0 and counter < len(self.pagelist):
           
           
            if tamanho > memoriaLivre:
                print(f"{processo.nome} nao pode ser alocado!")
                break
            
            if self.pagelist[counter].status == "Livre":
                tamanho -= self.pagelist[counter].size
                print(f"{processo.nome} ocupou a pagina {self.pagelist[counter].id}")
                self.pagelist[counter].status = "Ocupado"
                if tamanho < 0:
                    print(f"Houve fragmentacao interna de {abs(tamanho)} MBs  na pagina {self.pagelist[counter].id}")
                else:
                    print(f"Nao houve fragmentacao interna na pagina {self.pagelist[counter].id}")
            counter += 1

            


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

#Adiciono cada processo da lista a minha memória virtual:
for i in lista:
    memoria.add_processo(i)

#Aqui apenas printamos o status de cada pagina na minha memória virtual:
for x in memoria.pagelist:
    print(f"status da pagina {x.id} eh:",x.status)
