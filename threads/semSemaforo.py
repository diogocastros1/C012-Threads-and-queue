import threading
import time
import queue
import random

class Cliente:
    def __init__(self, id, tempo_atendimento):
        self.id = id
        self.tempo_atendimento = tempo_atendimento
        self.tempo_espera = 0

def fcfs(clientes):
    tempo_atual = 0
    for cliente in clientes:
        cliente.tempo_espera = tempo_atual
        print(f"Atendendo cliente {cliente.id} com tempo de atendimento {cliente.tempo_atendimento}")
        time.sleep(cliente.tempo_atendimento)  # Simulando tempo de atendimento
        tempo_atual += cliente.tempo_atendimento

def round_robin(clientes, quantum):
    fila = queue.Queue()
    for cliente in clientes:
        fila.put(cliente)
    
    tempo_atual = 0
    while not fila.empty():
        cliente = fila.get()
        if cliente.tempo_atendimento > quantum:
            cliente.tempo_atendimento -= quantum
            fila.put(cliente)
            print(f"Atendendo cliente {cliente.id} por {quantum} unidades de tempo")
            time.sleep(quantum)
            tempo_atual += quantum
        else:
            print(f"Atendendo cliente {cliente.id} por {cliente.tempo_atendimento} unidades de tempo")
            time.sleep(cliente.tempo_atendimento)
            tempo_atual += cliente.tempo_atendimento
        cliente.tempo_espera += tempo_atual - cliente.tempo_atendimento

def calcular_tempo_espera_medio(clientes):
    total_espera = sum(cliente.tempo_atendimento for cliente in clientes)
    return total_espera / len(clientes)

def main():
    # Criando lista de clientes
    clientes = [Cliente(i, random.randint(1, 5)) for i in range(10)]

    print("Simulando FCFS...")
    inicio_fcfs = time.time()
    fcfs(clientes)
    fim_fcfs = time.time()
    tempo_espera_medio_fcfs = calcular_tempo_espera_medio(clientes)
    tempo_execucao_fcfs = fim_fcfs - inicio_fcfs
    print(f"Tempo de espera médio FCFS: {tempo_espera_medio_fcfs:.2f} unidades de tempo")
    print(f"Tempo de execução FCFS: {tempo_execucao_fcfs:.2f} segundos\n")
    
    # Resetando tempos de espera dos clientes
    for cliente in clientes:
        cliente.tempo_espera = 0

    print("Simulando Round Robin...")
    quantum = 2
    inicio_rr = time.time()
    round_robin(clientes, quantum)
    fim_rr = time.time()
    tempo_espera_medio_rr = calcular_tempo_espera_medio(clientes)
    tempo_execucao_rr = fim_rr - inicio_rr
    print(f"Tempo de espera médio Round Robin: {tempo_espera_medio_rr:.2f} unidades de tempo")
    print(f"Tempo de execução Round Robin: {tempo_execucao_rr:.2f} segundos")

    # Comparação dos tempos de execução
    print("\nComparação dos tempos de execução:")
    if tempo_execucao_fcfs < tempo_execucao_rr:
        print(f"FCFS foi mais rápido por {tempo_execucao_rr - tempo_execucao_fcfs:.2f} segundos")
    elif tempo_execucao_fcfs > tempo_execucao_rr:
        print(f"Round Robin foi mais rápido por {tempo_execucao_fcfs - tempo_execucao_rr:.2f} segundos")
    else:
        print("Ambos os algoritmos levaram o mesmo tempo para executar")

if __name__ == "__main__":
    main()

