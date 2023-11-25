import random, os

CACHE_TAM = 16
MP_TAM = 2048
BLOCO_TAM = 16

class MemoriaCache:
    def __init__(self):
        self.dados = [0] * BLOCO_TAM
        self.rotulo = 0
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
    if 0 <= endereco < MP_TAM:
        global acessos, acertos, faltas, leituras

        acessos += 1

        index_cache = endereco % CACHE_TAM
        bloco = endereco // CACHE_TAM
        elemento = endereco % BLOCO_TAM

        endereco_bin = bin(endereco)
        bloco_bin = bin(bloco)

        print(f"Endereço da referência em binário: {endereco_bin}")
        print(f"Número do rótulo em binário: {bloco_bin}")

        if cache[index_cache].flag and cache[index_cache].rotulo == bloco:
            acertos += 1
        else:
            faltas += 1

            cache[index_cache].dados = mp[endereco // BLOCO_TAM].dados
            cache[index_cache].rotulo = bloco
            cache[index_cache].flag = True

        leituras += 1
        return cache[index_cache].dados[elemento]
    else:
        print("Endereço Inválido!")

def escreverMemoria(endereco, dado):
    if 0 <= endereco < MP_TAM:
        global  acessos, escritas, leituras

        acessos += 1

        index_cache = endereco % CACHE_TAM
        rotulo = endereco // CACHE_TAM
        elemento = endereco % BLOCO_TAM
        endereco_bin = bin(endereco)

        if cache[index_cache].flag and cache[index_cache].rotulo:
            cache[index_cache].dados[elemento] = dado
        else:
            leituras += 1
            cache[index_cache].dados = mp[endereco // BLOCO_TAM].dados.copy()
            cache[index_cache].dados[elemento] = dado
            cache[index_cache].rotulo = rotulo
            cache[index_cache].flag = True
        
        escritas += 1
        return endereco_bin
    else:
        print("Endereço Inválido!")

while True:
    print("1 - Ler memória")
    print("2 - Escrever memória")
    print("3 - Exibir estatísticas")
    print("0 - Sair")
    op = int(input("Entre com sua opção: "))
    match op:
        case 0:
            break
        case 1:
            endereco = int(input("Entre com o endereço de memória que deseja consultar: "))
            lido = lerMemoria(endereco)
            print(f"Dado lido na memória: {lido}")
        case 2:
            endereco = int(input("Entre com o endereço de memória que deseja escrever: "))
            dado = input("Entre com o dado que deseja escrever: ")
            escrito = escreverMemoria(endereco, dado)
            print(f"O dado {dado} foi escrito no endereço de memória número {escrito}!")    
        
        case 3:
            print(f"Total de acessos: {acessos}")
            print(f"Total de acertos: {acertos}")
            print(f"Total de faltas: {faltas}")
            print(f"Total de leituras na memória: {leituras}")
            print(f"Total de escritas na memória: {escritas}")
        case _:
            print("Opção inválida!!")
    
    input("Aperte qualquer tecla para continuar")
    os.system('cls') # Se usar o GNU Debugger, utilizar ('clear') ao invés de ('cls')