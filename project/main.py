import json

# Pode listar, adicionar e marcar como concluídas


def listarTarefas(task):

    size = len(task)

    objectt = {'Tarefas':[], 
               'Concluida':[]}
    
    for x in task:
        objectt['Tarefas'].append(x['titulo'])
        objectt['Concluida'].append(x['concluida'])
    
    result = lambda x: "feita" if x == True else "A fazer"

    print("")
    for i in range(0, size):
        print(f"  Tarefa: {objectt['Tarefas'][i]}: Estado: {result(objectt['Concluida'][i])}")
    
    print(f" -- Número de tarefas na lista {size} --\n")

def readJson():

    with open('db.json', 'r') as arquivo:
        task = json.load(arquivo)
        #output [{'id': 1, 'titulo': 'Estudar Python', 'concluida': False}, {'id': 2, 'titulo': 'Assistir vÃ\xaddeo sobre Docker', 'concluida': True}]

        listarTarefas(task)

#readJson()
# Essa função ira ler o arquivo json, e organizar os dados para serem exibidos para o usuário.

def add():

    model =     {
        "id": 4,
        "titulo": "teste",
    }

    with open('db.json', 'r') as arquivo:
        tarefas = json.load(arquivo)

        tarefas.append(model)

    with open('db.json', 'w') as file:
        json.dump(tarefas, file, indent=4)

add()
