import threading
from pymongo import MongoClient
from caixa import cria_fila_caixa, atendimento_cliente

# Configurações do banco de dados
MONGODB_URL = 'mongodb+srv://root:6qAsN$-!8sUPVbg@cluster0.slkiyz1.mongodb.net/test'
DB_NAME = 'supermarket'

# # Conexão com o banco de dados
client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
treads = []

# Conexão com o banco de dados (substitua pelas suas configurações)
caixas_collection = db.caixas

# Criando caixas
caixas = ['Caixa1']
for caixa in caixas:
  cria_fila_caixa(caixa, caixas_collection)

# Iniciando atendimento nos caixas
for caixa in caixas:
  t = threading.Thread(target=atendimento_cliente, args=(caixa, 5, caixas_collection))
  t.start()

# Aguardando todos os caixas serem fechados
for t in threads:
  t.join()

print("Todos os caixas foram fechados.")