import threading
import time
import queue
import random

#Classe Cliente:
class Cliente:
    def __init__(self, id, tempo_atendimento):
        self.id = id
        self.tempo_atendimento = tempo_atendimento
        self.tempo_espera = 0

class Caixa:
    def __init__(self, id):
        self.id = id
        self.semaphore = threading.Semaphore(1)  # Semáforo binário (mutex)
    
    def atender_cliente(self, cliente):
        with self.semaphore:
            print(f"Caixa {self.id} atendendo cliente {cliente.id} com tempo de atendimento {cliente.tempo_atendimento}")
            time.sleep(cliente.tempo_atendimento)  # Simulando tempo de atendimento
            print(f"Caixa {self.id} terminou de atender cliente {cliente.id}")


def caixa_thread(caixa, fila_clientes):
    while not fila_clientes.empty():
        cliente = fila_clientes.get()
        caixa.atender_cliente(cliente)
        fila_clientes.task_done()


def fcfs(clientes):
    fila_clientes = queue.Queue()
    for cliente in clientes:
        fila_clientes.put(cliente)
    
    caixas = [Caixa(i) for i in range(3)]  # Exemplo com 3 caixas
    threads = []
    
    for caixa in caixas:
        t = threading.Thread(target=caixa_thread, args=(caixa, fila_clientes))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def round_robin(clientes, quantum):
    fila_clientes = queue.Queue()
    for cliente in clientes:
        fila_clientes.put(cliente)
    
    caixas = [Caixa(i) for i in range(3)]  # Exemplo com 3 caixas
    threads = []
    
    def caixa_rr_thread(caixa):
        while not fila_clientes.empty():
            cliente = fila_clientes.get()
            if cliente.tempo_atendimento > quantum:
                print(f"Caixa {caixa.id} atendendo cliente {cliente.id} por {quantum} unidades de tempo")
                cliente.tempo_atendimento -= quantum
                time.sleep(quantum)
                fila_clientes.put(cliente)
            else:
                print(f"Caixa {caixa.id} atendendo cliente {cliente.id} por {cliente.tempo_atendimento} unidades de tempo")
                time.sleep(cliente.tempo_atendimento)
            fila_clientes.task_done()
    
    for caixa in caixas:
        t = threading.Thread(target=caixa_rr_thread, args=(caixa,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


def calcular_tempo_espera_medio(clientes):
    total_espera = sum(cliente.tempo_atendimento for cliente in clientes)
    return total_espera / len(clientes)

def main():
    # Criando lista de clientes
    clientes = [Cliente(i, random.randint(1, 5)) for i in range(10)]
    
    # Simulando FCFS
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

    # Simulando Round Robin
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



