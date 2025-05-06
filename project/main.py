import json
import os 

# Pode listar, adicionar e marcar como concluídas

def listarTarefas(task):
    # Função responsável por organizar as informações lidas do arquivo json.

    size = len(task)

    objectt = {'Tarefas':[], 
               'Concluida':[]}
    
    for x in task:
        objectt['Tarefas'].append(x['titulo'])
        objectt['Concluida'].append(x['concluida'])
    
    result = lambda x: "feita" if x == True else "A fazer"

    print("")
    for i in range(0, size):
        print(f"{i + 1}  Tarefa: {objectt['Tarefas'][i]}: Estado: {result(objectt['Concluida'][i])}")
    
    print(f"\n -- Número de tarefas na lista {size} --\n")

def readJson():
    # Essa função irá ler o arquivo json, e organizar os dados para serem exibidos para o usuário.

    with open('db.json', 'r') as arquivo:
        task = json.load(arquivo)
        listarTarefas(task)

def add_task(tarefa):
    # Essa função adiciona uma nova tarefa na lista de tarefas.

    with open('db.json', 'r') as idd:
        task = json.load(idd)
        size = len(task)
        obj = task[size - 1]
    
    try:
        with open('db.json', 'r') as idd:
            task = json.load(idd)
            size = len(task)
            obj = task[size - 1]

            id = obj['id'] + 1
            
    except Exception as e:
        print(f"Erro ao pegar id {e}")

    model =     {
        'id': id,
        'titulo': tarefa,
        'concluida':False
    }

    with open('db.json', 'r') as arquivo:
        tarefas = json.load(arquivo)

        tarefas.append(model)

    with open('db.json', 'w') as file:
        json.dump(tarefas, file, indent=4)
    
    return print("-- Tarefa adicionada com sucesso --\n")

def mark(id):
    # Função responsável por marcar o estado de uma tarefa

    try:
        with open ('db.json', 'r') as file:
            db = json.load(file)
            size = 0
            for i in db:
                if id == i['id']:
                    db[size]['concluida'] = True
                size += 1
        
        with open('db.json', 'w')as arquivo:
            json.dump(db, arquivo, indent=4)

            return print("Tarefa marcada como conluida com sucesso")
        
    except Exception as e:
        print(f"Erro ao pegar id:{id}")

def main():
    # Função responsável por gerenciar todas as outras funções, como chamar e passar parâmetros.

    ope = " -- To-do --\n Escolha uma opção\n 1 - adicionar\n 2 - Listar tarefas\n 3 - Marcar como concluida\n 4 - Encerrar o programa"

    n = 0

    while n < 4:

        print(ope)
        chose = int(input())

        if chose == 1:
            os.system("cls")
            print("Escreva a tarefa que deseja adicionar: ")
            tarefa = str(input())
            add_task(tarefa)

        elif chose == 2:
            os.system("cls")
            readJson()

        elif chose == 3:
            os.system("cls")
            #print("Digite o número da tarefa que deseja marcar como conluida: ")
            readJson()
            id = int(input("Escolha o número da tarefa que deseja concluir: "))
            mark(id)

        elif chose == 4:
            n = 5
            print("Fim do programa")
        else:
            print("Digite um número valido")
       
main()
