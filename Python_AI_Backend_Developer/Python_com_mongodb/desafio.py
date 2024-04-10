import pymongo

# Conectando ao servidor MongoDB, servidor tem que está online
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.3")

# Escolha o banco de dados (criará um novo se não existir)
db = client["usuarios"]

# Coleção
collection = db["pessoas"]


# Função para inserir um novo usuário
def criar_usuario(nome, idade, email):
    usuario = {"nome": nome, "idade": idade, "email": email}
    collection.insert_one(usuario)
    print("Usuário criado com sucesso.")


# Função para listar todos os usuários
def listar_usuarios():
    usuarios = collection.find()
    for usuario in usuarios:
        print(usuario)


# Função para encontrar um usuário por email
def encontrar_usuario_por_email(email):
    usuario = collection.find_one({"email": email})
    if usuario:
        print(usuario)
    else:
        print("Usuário não encontrado.")


# Função para atualizar a idade de um usuário por email
def atualizar_idade_do_usuario(email, nova_idade):
    collection.update_one({"email": email}, {"$set": {"idade": nova_idade}})
    print("Idade do usuário atualizada com sucesso.")


# Função para excluir um usuário por email
def excluir_usuario(email):
    collection.delete_one({"email": email})
    print("Usuário excluído com sucesso.")


# Exemplo de uso das funções
criar_usuario("João", 30, "joao@example.com")
criar_usuario("Maria", 25, "maria@example.com")

listar_usuarios()

encontrar_usuario_por_email("joao@example.com")

atualizar_idade_do_usuario("joao@example.com", 35)
listar_usuarios()

excluir_usuario("joao@example.com")
listar_usuarios()

# Fechar conexão com o cliente MongoDB quando terminar
client.close()
