def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("---> Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    print("-" * 50)
    print(f{' ' * 15}"Lista de tarefas:"{' ' * 15})
    print("-" * 50)
    i = 1
    for tarefa in lista_de_tarefas:
        print(f"{i} - {tarefa}")
        i += 1
    print("-" * 50)

def exibir_menu():
    print("Escolha uma opção:\n" \
    "1 - Inserir uma nova tarefa\n" \
    "2 - Listar tarefas\n" \
    "3 - Deletar tarefa\n" \
    "4 - Sair"
    )

def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop((tarefa - 1))
    print('Tarefa deletada!')
    return lista_de_tarefas

lista_de_tarefas = list()
continuar = True
print("Bem-vind@ à sua lista de tarefas!")
print("-" * 50)
print('\n')
while True:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)

    elif opcao == '3':
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric(): 
            print("Número inválido! Tente novamente.")
        if int(tarefa) > len(lista_de_tarefas):
            print("Número inválido! Tente novamente.")
        elif int(tarefa) <= 0:
            print("Número inválido! Tente novamente.")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))

    elif opcao == "4":
        continuar = False

    else:
        print("Opção inválida!")
    print('\n')

