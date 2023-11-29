# Alunos: Daniel Fernando Vieira e Carlos Eduardo Da Silva Cé

import random, os

CACHE_TAM = 16
MP_TAM = 2048
BLOCO_TAM = 16

class MemoriaCache:
    def __init__(self):
        self.dados = [0] * BLOCO_TAM
        self.rotulo = -1
        self.flag = False

class MemPrincipal:
    def __init__(self):
        self.dados = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(BLOCO_TAM)]

cache = [MemoriaCache() for _ in range(CACHE_TAM)]
mp = [MemPrincipal() for _ in range(MP_TAM)]
acessos = 0
acertos = 0
faltas = 0
leituras = 0
escritas = 0

def lerMemoria(endereco):
    endereco_dec = int(endereco, 2)
    if 0 <= endereco_dec < MP_TAM:
        global acessos, acertos, faltas, leituras

        acessos += 1
        
        bloco = endereco_dec // CACHE_TAM
        index_cache = bloco % CACHE_TAM
        elemento = endereco_dec % BLOCO_TAM

        bloco_bin = bin(bloco)

        print(f"Endereço da referência em decimal: {endereco_dec}")
        print(f"Número do rótulo em binário: {bloco_bin}")

        if cache[index_cache].flag and cache[index_cache].rotulo == bloco:
            acertos += 1
        else:
            faltas += 1

            cache[index_cache].dados = mp[endereco_dec // BLOCO_TAM].dados
            cache[index_cache].rotulo = bloco
            cache[index_cache].flag = True

        leituras += 1
        return cache[index_cache].dados[elemento]
    else:
        print("Endereço Inválido!")

def escreverMemoria(endereco, dado):
    endereco_dec = int(endereco, 2)
    if 0 <= endereco_dec < MP_TAM:
        global  acessos, escritas, leituras, acertos, faltas

        acessos += 1
        
        rotulo = endereco_dec // CACHE_TAM
        index_cache = rotulo % CACHE_TAM
        elemento = endereco_dec % BLOCO_TAM

        if cache[index_cache].flag and cache[index_cache].rotulo:
            cache[index_cache].dados[elemento] = dado
        else:
            acertos += 1
            leituras += 1
            cache[index_cache].dados = mp[endereco_dec // BLOCO_TAM].dados.copy()
            cache[index_cache].dados[elemento] = dado
            cache[index_cache].rotulo = rotulo
            cache[index_cache].flag = True
        
        escritas += 1
        return endereco_dec
    else:
        print("Endereço Inválido!")
    
def mostrarCache():
    for i, bloco in enumerate(cache):
        print(f"Quadro {i}:")
        print(f"Rótulo: {bloco.rotulo}")
        print(f"Dados: {bloco.dados}\n")

while True:
    print("1 - Ler memória")
    print("2 - Escrever memória")
    print("3 - Exibir estatísticas")
    print("4 - Exibir memória cache")
    print("0 - Sair")
    op = int(input("Entre com sua opção: "))
    match op:
        case 0:
            break
        case 1:
            endereco = input("\nEntre com o endereço de memória em binário que deseja consultar: ")
            lido = lerMemoria(endereco)
            print(f"Dado lido na memória: {lido}")
        case 2:
            endereco = input("\nEntre com o endereço de memória em binário que deseja escrever: ")
            dado = input("Entre com o dado que deseja escrever: ")
            escrito = escreverMemoria(endereco, dado)
            print(f"O dado {dado} foi escrito no endereço de memória número {escrito}!")    
        
        case 3:
            print(f"\nTotal de acessos: {acessos}")
            print(f"Total de acertos: {acertos}")
            print(f"Total de faltas: {faltas}")
            print(f"Total de leituras na memória: {leituras}")
            print(f"Total de escritas na memória: {escritas}")
        
        case 4:
            mostrarCache()
            
        case _:
            print("Opção inválida!!")
    
    input("Aperte qualquer tecla para continuar")
    os.system('clear') # Se usar o GNU Debugger, utilizar ('clear') ao invés de ('cls')
    