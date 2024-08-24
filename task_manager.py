import os  # Importa o módulo os para usar comandos do sistema operacional

def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as file:  # Tenta abrir o arquivo 'tarefas.txt' em modo de leitura
            return file.readlines()  # Retorna uma lista com as linhas do arquivo
    except FileNotFoundError:  # Se o arquivo não for encontrado
        return []  # Retorna uma lista vazia

def salvar_tarefas(tarefas):
    with open('tarefas.txt', 'w') as file:  # Abre o arquivo 'tarefas.txt' em modo de escrita
        file.writelines(tarefas)  # Escreve a lista de tarefas no arquivo

def adicionar_tarefas(descricao):
    tarefas = carregar_tarefas()  # Carrega as tarefas existentes
    tarefas.append(descricao + "\n")  # Adiciona a nova tarefa à lista
    salvar_tarefas(tarefas)  # Salva a lista atualizada de tarefas
    os.system("cls")  # Limpa a tela (no Windows)
    print("Adicionado com Sucesso !!!")  # Informa que a tarefa foi adicionada com sucesso

def listar_tarefas():
    tarefas = carregar_tarefas()  # Carrega as tarefas existentes
    if tarefas:  # Se houver tarefas
        for i, tarefa in enumerate(tarefas, 1):  # Enumera e imprime cada tarefa
            print(f"{i}. {tarefa.strip()}")  # Imprime o número e a descrição da tarefa
    else:
        os.system("cls")  # Limpa a tela (no Windows)
        print("Nenhuma tarefa encontrada.")  # Informa que não há tarefas

def remover_tarefas(indice):
    tarefas = carregar_tarefas()  # Carrega as tarefas existentes
    if 0 < indice <= len(tarefas):  # Verifica se o índice é válido
        tarefas.pop(indice - 1)  # Remove a tarefa pelo índice
        salvar_tarefas(tarefas)  # Salva a lista atualizada de tarefas
        os.system("cls")  # Limpa a tela (no Windows)
        print("Removido com sucesso !!")  # Informa que a tarefa foi removida com sucesso
    else:
        os.system("cls")  # Limpa a tela (no Windows)
        print("Erro ao Remover !!")  # Informa que houve um erro ao remover a tarefa

while True:
    print("======================")
    print("====== SISTEMA =======")
    print("== GERENCIAR TAREFA ==")
    print("======================")
    print("1 - ADICIONAR TAREFA")
    print("2 - LISTAR TAREFAS")
    print("3 - REMOVER TAREFA")
    print("4 - SALVAR E SAIR")
    escolha = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção
    os.system("cls")  # Limpa a tela (no Windows)
    if escolha == "1":
        descricao = input("Digite uma descrição para a tarefa: ")  # Solicita a descrição da nova tarefa
        adicionar_tarefas(descricao)  # Adiciona a nova tarefa
    elif escolha == "2":
        listar_tarefas()  # Lista todas as tarefas
    elif escolha == "3":
        listar_tarefas()  # Lista todas as tarefas
        try:
            indice = int(input("Digite o número para remover a tarefa: "))  # Solicita o índice da tarefa a ser removida
            remover_tarefas(indice)  # Remove a tarefa pelo índice
        except ValueError:
            print("Por favor, digite o número corretamente.")  # Informa que o valor digitado não é um número válido
    elif escolha == "4":
        break  # Sai do loop e encerra o programa
    else:
        print("Digite a opção correta !!")  # Informa que a opção digitada é inválida