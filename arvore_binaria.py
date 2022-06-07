class No(object):
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


class Arvore(object):
    def __init__(self):
        self.raiz = None
        self.cont_espaco = 10

    def inserir(self, chave: int) -> None:
        # cria um novo Nó
        novo = No(chave)
        if self.raiz == None:
            self.raiz = novo
        # se nao for a raiz
        else:
            atual = self.raiz
            while True:
                anterior = atual
                # ir para esquerda
                if chave <= atual.chave:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                # ir para direita
                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

    def remover(self, chave):
        if self.raiz == None:
            return False  # se arvore vazia
        atual = self.raiz
        pai = self.raiz
        filho_esq = True
        # ****** Buscando o valor **********
        while atual.item != chave:  # enquanto nao encontrou
            pai = atual
            if chave < atual.item:  # caminha para esquerda
                atual = atual.esq
                filho_esq = True  # é filho a esquerda? sim
            else:  # caminha para direita
                atual = atual.dir
                filho_esq = False  # é filho a esquerda? NAO
            if atual == None:
                return False  # encontrou uma folha -> sai
        # fim laço while de busca do valor

        # **************************************************************
        # se chegou aqui quer dizer que encontrou o valor (chave)
        # "atual": contem a referencia ao No a ser eliminado
        # "pai": contem a referencia para o pai do No a ser eliminado
        # "filho_esq": é verdadeiro se atual é filho a esquerda do pai
        # **************************************************************

        # Se nao possui nenhum filho (é uma folha), elimine-o
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None  # se raiz
            else:
                if filho_esq:
                    pai.esq = None  # se for filho a esquerda do pai
                else:
                    pai.dir = None  # se for filho a direita do pai

        # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq  # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.esq  # se for filho a esquerda do pai
                else:
                    pai.dir = atual.esq  # se for filho a direita do pai

        # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir  # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.dir  # se for filho a esquerda do pai
                else:
                    pai.dir = atual.dir  # se for  filho a direita do pai

        # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        else:
            sucessor = self.nosucessor(atual)
            # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
            if atual == self.raiz:
                self.raiz = sucessor  # se raiz
            else:
                if filho_esq:
                    pai.esq = sucessor  # se for filho a esquerda do pai
                else:
                    pai.dir = sucessor  # se for filho a direita do pai
            sucessor.esq = atual.esq  # acertando o ponteiro a esquerda do sucessor agora que ele assumiu
            # a posição correta na arvore
        return True

    def busca(self, chave):
        # adiciona a função interna
        def _busca(self, no: No, chave: int) -> No:
            if no != None:
                # print("Visitou chave: {}".format(no.chave))
                if no.chave == chave:
                    return no
                elif chave <= no.chave:
                    return self._busca(no.esq, chave)
                elif chave > no.chave:
                    return self._busca(no.dir, chave)
            return None

        # chama a função interna
        return self._busca(self.raiz, chave)

    def busca_recursiva(self, chave):
        return self._busca_recursiva(self.raiz, chave)

    def _busca_recursiva(self, no: No, chave: int):
        if no != None:
            print("Visitou chave: {}".format(no.chave))
            if no.chave == chave:
                return True
            elif chave <= no.chave:
                return self._busca_recursiva(no.esq, chave)
            elif chave > no.chave:
                return self._busca_recursiva(no.dir, chave)
        return False

    def busca_iterativa(self, chave: int):
        return self._busca_iterativa(self.raiz, chave)

    def _busca_iterativa(self, no: No, chave: int):
        if no != None:
            no_atual = no
            while no_atual != None:
                print("Visitou chave: {}".format(no_atual.chave))
                if no_atual.chave == chave:
                    return True
                elif chave <= no_atual.chave:
                    no_atual = no_atual.esq
                else:
                    no_atual = no_atual.dir

            return False

    def imprimir_arvore(self, raiz=None, espaco=0):
        # Base case
        if (raiz == None):
            return
        # Increase distance between levels
        espaco += self.cont_espaco

        # Process right child first
        self.imprimir_arvore(raiz.dir, espaco)

        # Print current node after space
        print(end=" " * (espaco - self.cont_espaco))
        print(raiz.chave)
        # Process left child
        self.imprimir_arvore(raiz.esq, espaco)

    def altura(self, no: No) -> int:
        altura_dir, altura_esq = 0, 0
        if no == None:
            return -1
        else:
            altura_dir = self.altura(no.dir)
            altura_esq = self.altura(no.esq)
        return (altura_dir + 1) if (altura_dir > altura_esq) else altura_esq + 1


if __name__ == "__main__":

    lista = [115, 98, 34, 56, 100, 25, 132, 130, 133, 55]

    arvore = Arvore()
    for i in lista:
        arvore.inserir(i)

    print("Impressão da árvore: \n")
    arvore.imprimir_arvore(arvore.raiz)

    arvore.remover(55)
    arvore.imprimir_arvore(arvore.raiz)
    print("Altura da árvore: {}".format(arvore.altura(arvore.raiz)))