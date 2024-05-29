# Projeto C012 - Sistema com threads

## Implementação no Contexto do Código

#### Classe Caixa

Cada caixa é uma instância da classe Caixa, que contém um semáforo binário (`threading.Semaphore(1)`). Este semáforo é utilizado para controlar o acesso ao método `atender_cliente`.

#### Método `atender_cliente`

O método `atender_cliente` usa o semáforo para garantir que apenas uma thread possa executar o bloco de código dentro do `with self.semaphore:` de cada vez. Quando uma thread entra no bloco, ela "adquire" o semáforo, bloqueando outras threads até que ela libere o semáforo (saia do bloco).

#### Função `caixa_thread`

Cada thread de caixa chama o método `caixa_thread`, que tenta continuamente atender clientes da fila até que ela esteja vazia. O semáforo dentro do método `atender_cliente` garante que mesmo que várias threads tentem atender clientes ao mesmo tempo, cada caixa só atende um cliente por vez.

### Como o Semáforo Funciona em FCFS e Round Robin

#### FCFS (First Come First Served)

* As threads de caixas são iniciadas e cada uma tenta pegar um cliente da fila.
* Quando uma thread chama `caixa.atender_cliente(cliente)`, o semáforo garante que o código dentro do método `atender_cliente` seja executado exclusivamente por uma thread por vez.
* Cada caixa atende um cliente de cada vez, na ordem em que os clientes estão na fila.

#### Round Robin

* As threads de caixas são iniciadas e cada uma tenta pegar um cliente da fila.
* Quando uma thread chama `caixa_rr_thread`, ela atende o cliente por um tempo definido pelo quantum.
* Se o tempo de atendimento restante do cliente for maior que o quantum, ele é colocado de volta na fila.
* O semáforo dentro do método `atender_cliente` ainda garante que cada caixa só atende um cliente de cada vez, mesmo que o atendimento seja interrompido e retomado.

## Semáforo em Python

Um semáforo é uma estrutura de sincronização que é utilizada para controlar o acesso a um recurso compartilhado em um ambiente multi-thread. Ele pode ser visto como uma espécie de contador que controla o número de threads que podem acessar um recurso ao mesmo tempo.

## Semáforo Binário (Mutex)

No nosso código, estamos usando um semáforo binário (mutex) para garantir que cada caixa atenda apenas um cliente por vez. Isso impede que múltiplas threads acessem a seção crítica simultaneamente, garantindo a exclusão mútua.

### Resumo

O semáforo é crucial para garantir a exclusão mútua, ou seja, que cada caixa atenda apenas um cliente por vez. Isso previne condições de corrida e garante que o atendimento dos clientes seja ordenado e seguro. Ao utilizar o semáforo dentro do método `atender_cliente`, asseguramos que múltiplas threads (caixas) possam tentar acessar o recurso compartilhado (fila de clientes), mas somente uma thread por caixa execute a seção crítica do código de atendimento de cada vez.
