# Define as funções
def adicionar_tarefa(lista_de_tarefas, tarefa):
    # Adiciona nova tarefa para a lista.
    lista_de_tarefas.append(tarefa)
    print("---> Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    #Exibe a lista de tarefas
    print('\n')
    print("-" * 50)
    print(f"{' ' * 15}Lista de tarefas:{' ' * 15}")
    print("-" * 50)
    i = 1
    for tarefa in lista_de_tarefas:
        print(f"{i} - {tarefa}")
        i += 1
    print("-" * 50)

def exibir_menu():
    #Exibe o menu
    print("-" * 50)
    print("Escolha uma opção:\n" \
    "1 - Inserir uma nova tarefa\n" \
    "2 - Listar tarefas\n" \
    "3 - Deletar tarefa\n" \
    "4 - Sair"
    )
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    #Deleta tarefa da lista existente a partir do numero
    lista_de_tarefas.pop((tarefa - 1))
    print('Tarefa deletada!')
    return lista_de_tarefas

def tarefa_valida(tarefa, lista_de_tarefas):
    #Valida a existencia da tarefa a ser deletada
    if not tarefa.isnumeric():
        return False
    numero = int(tarefa)
    if numero <= 0 or numero > len(lista_de_tarefas):
        return False
    return True

lista_de_tarefas = list()
continuar = True
print("-" * 50)
print("Bem-vind@ à sua lista de tarefas!")
print("-" * 50)
print('\n')

#Loop principal
while True:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)

    elif opcao == '3':
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if tarefa_valida(tarefa, lista_de_tarefas):
             deletar_tarefa(lista_de_tarefas, int(tarefa))
        else:
            print("Número inválido! Tente novamente.")

    elif opcao == "4":
        continuar = False

    else:
        print("Opção inválida!")
    print('\n')