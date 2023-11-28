#Referencia - https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/arvores/

import os
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)
class ArvoreBinaria:
    def __init__(self):
        self.inicio = None
        
    def ArvoreVazia(self,raiz):
        return raiz == None
        
    def insere(self, raiz, nodo):
        """Insere um nodo em uma �rvore bin�ria de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo
        # Nodo deve ser inserido na sub�rvore direita.
        elif int(nodo.chave) > int(raiz.chave):
            print(raiz.chave," -> ",nodo.chave)
            print('Inseriu a direita')
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)
        # Nodo deve ser inserido na sub�rvore esquerda. 
        else:
            print(nodo.chave," <- ",raiz.chave)
            print('Inseriu a esquerda')
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)
                
    def pre_ordem(self, raiz):
        if not raiz:
            return
        # Visita nodo corrente.
        #print(raiz)
        print(raiz.__repr__())
        # Visita filho da esquerda.
        self.pre_ordem(raiz.esquerda)
        # Visita filho da direita.
        self.pre_ordem(raiz.direita)
        
    def in_ordem(self, raiz):
        if not raiz:
            return
        self.in_ordem(raiz.esquerda)
        print(raiz.__repr__())
        self.in_ordem(raiz.direita)
        
    def pos_ordem(self, raiz):
        if not raiz:
            return
        self.pos_ordem(raiz.esquerda)
        self.pos_ordem(raiz.direita)
        print(raiz.__repr__())

    def contarNodoInterno(self, raiz):
        if self.ArvoreVazia(raiz) or (raiz.esquerda is None and raiz.direita is None):
            return 0
        return 1 + self.contarNodoInterno(raiz.esquerda) + self.contarNodoInterno(raiz.direita)
    
    def exibirNodoInterno(self, raiz):
        if self.ArvoreVazia(raiz):
            return
        if raiz.esquerda is not None or raiz.direita is not None:
            print(raiz)
        self.exibirNodoInterno(raiz.esquerda)
        self.exibirNodoInterno(raiz.direita)
    
    def contarNodoPar(self, raiz):
        if self.ArvoreVazia(raiz):
            return 0
        par = 0
        if raiz.chave is not None and int(raiz.chave) % 2 == 0:
            par = 1
        
        return par + self.contarNodoPar(raiz.esquerda) + self.contarNodoPar(raiz.direita)

    def somarNodoImpar(self, raiz):
        if self.ArvoreVazia(raiz):
            return 0
        impar = 0
        if raiz.chave is not None and int(raiz.chave) % 2 != 0:
            impar += int(raiz.chave)
        return impar + self.somarNodoImpar(raiz.esquerda) + self.somarNodoImpar(raiz.direita)
    
    def encontrarNivel(self, raiz, num, nivel = 0):
        if self.ArvoreVazia(raiz):
            return -1 
        if int(raiz.chave) == num:
            return nivel
        
        nivel_encontrado = self.encontrarNivel(raiz.esquerda, num, nivel + 1)
        if nivel_encontrado != -1:
            return nivel_encontrado
        nivel_encontrado = self.encontrarNivel(raiz.direita, num, nivel + 1)
        return nivel_encontrado

Arvore = ArvoreBinaria()
raiz = None
while True:
    os.system('cls') # Se for rodar no GDB utilizar ('clear'), cls só funciona no VSCode
    print("1 - Inserir um nodo na árvore.")
    print("2 - Percorrer a árvore em: PRÉ-FIXADO.")
    print("3 - Percorrer a árvore em: INFIXADO.")    
    print("4 - Percorrer a árvore em: PÓS-FIXADO.")
    print("5 - Mostrar e contar quantos nodos internos tem a árvore.")
    print("6 - Contar quantos nós os valores são pares.")
    print("7 - Somar os nós impares.")
    print("8 - Entrar com um número e dizer o nível que ele se encontra (pode ter mais que um).")
    print("0 - Sair.")
    OP = int(input("Entre com a operação desejada: "))
    if OP == 0:
        break
    elif OP == 1:
        valor = input("Entre com o valor: ")
        if Arvore.ArvoreVazia(raiz):
            print('Nodo Raiz')
            raiz = NodoArvore(valor)
        else:
            nodo = NodoArvore(valor)
            Arvore.insere(raiz,nodo)        
    elif OP == 2:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pre_ordem(raiz)        
    elif OP == 3:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.in_ordem(raiz)                
    elif OP == 4:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")                       
        Arvore.pos_ordem(raiz)
    elif OP == 5:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")
        else:
            nodos_internos = Arvore.contarNodoInterno(raiz)
            print(f"A árvore possui {nodos_internos} nodos internos!")
            print("Nodos internos: ")
            Arvore.exibirNodoInterno(raiz)
    elif OP == 6:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")
        else:
            total_par = Arvore.contarNodoPar(raiz)
            print(f"A árvore possui {total_par} nodos pares!")
    elif OP == 7:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")
        else:
            soma_impar = Arvore.somarNodoImpar(raiz)
            print(f"A soma de todos os nodos ímpares é igual à {soma_impar}!")
    elif OP == 8:
        if Arvore.ArvoreVazia(raiz):
            print("ÁRVORE VAZIA!!!!!!!!!!!")
        else:
            num = int(input("Entre com o número à ser procurado: "))
            nivel_encontrado = Arvore.encontrarNivel(raiz, num)
            if nivel_encontrado == -1:
                print(f"O número {num} não foi detectado na árvore!")
            else:
                print(f"O número {num} foi detectado no nível {nivel_encontrado} dessa árvore!")
    else:
      print("OPCAO INVALIDA!!!!!!!!!!!")                       
    input("Digite uma tecla para continuar.")  