import random
import time

from Encomenda import Encomenda
from Veiculo import Veiculo
from PontoDeRedistribuicao import PontoDeRedistribuicao
from interface_monitoramento import Interface
from constants import *

# time.sleep = lambda x: None

def main():
    Interface().start()

    if not (P > A > C):
        print(f'[ERRO] P = {P}, A = {A}, C = {C} não satisfazem P > A > C\n')
        return

    for i in range(S):
        PontoDeRedistribuicao.pontos_de_redistribuicao.append(PontoDeRedistribuicao(i))

    for i in range(P):
        origem = random.randint(0, S - 1)
        destino = random.randint(0, S - 1)
        while origem == destino:
            destino = random.randint(0, S - 1)
        Encomenda.encomendas.append(Encomenda(i, origem, destino))
        PontoDeRedistribuicao.pontos_de_redistribuicao[origem].aguardando_transporte.append(Encomenda.encomendas[-1])
        Encomenda.encomendas[-1].t_origem = time.time()

    for i in range(C):
        veiculo = Veiculo(i, A, S, PontoDeRedistribuicao.pontos_de_redistribuicao)
        Veiculo.veiculos.append(veiculo)
        PontoDeRedistribuicao.pontos_de_redistribuicao[veiculo.ponto_de_redistribuicao].estacionar(veiculo)

    print('Iniciando simulação')
    for i in PontoDeRedistribuicao.pontos_de_redistribuicao:
        i.start()

    for i in Veiculo.veiculos:
        i.start()
        i.join()

    for i in PontoDeRedistribuicao.pontos_de_redistribuicao:
        i.stop()

    print('veiculos finalizados')
    print('Simulação finalizada')

if __name__ == '__main__' :
    main()