import time
import random

def cria_fila_caixa(nome_caixa, database):
    caixa_doc = {
        'nomeCaixa': nome_caixa,
        'clientesNaFila': 0,
        'caixaAberto': True
    }
    database.insert_one(caixa_doc)

def atendimento_cliente(nome_caixa, intervalo, database):
    while True:
        # Simulando chegada de clientes
        clientes = random.randint(0, 5)
        print(f"{clientes} cliente(s) chegaram ao caixa {nome_caixa}")

        # Atualizando o número de clientes na fila
        database.update_one({'nomeCaixa': nome_caixa}, {'$inc': {'clientesNaFila': clientes}})

        # Simulando atendimento
        if clientes > 0:
            print(f"1 cliente atendido no caixa {nome_caixa}")
            time.sleep(intervalo)
            print(f"Atendimento concluido no caixa {nome_caixa}\n")
            database.update_one({'nomeCaixa': nome_caixa}, {'$inc': {'clientesNaFila': -1}})

        # Verificando se o caixa deve ser fechado
        if clientes == 0:
            print(f"Caixa {nome_caixa} está vazio. Fechando o caixa.")
            database.update_one({'nomeCaixa': nome_caixa}, {'$set': {'caixaAberto': False}})
            break