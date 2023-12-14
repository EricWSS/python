from db_helper import DBHelper


def inserirTarefa(): #CREATE
    print()
    conn = DBHelper()
    tarefa = input("Digite a tarefa a ser inserida: ")
    sql = f"INSERT INTO ew_todolist (id, tarefa, feito) VALUES (Null, '{tarefa}', 1)"
    conn.execute(sql)

def listarTarefas(): # READ
    print()
    conn = DBHelper()
    tarefas = conn.execute("SELECT * FROM ew_todolist")
    for task in tarefas:
        if task[2]==0:
            print(f"\x1b[9mId:{task[0]} | {task[1]} | FEITO \x1b[0m")
        else:print(f"Id:{task[0]} | {task[1]} ")

def atualizarTarefa(): # UPDATE
    print()
    conn= DBHelper()
    listarTarefas()
    print()
    id_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
    tarefa = input("Digite a tarefa atualizada: ")
    sql = conn.execute(f"UPDATE ew_todolist SET tarefa={tarefa} WHERE id={id_tarefa}") 
    print()
    listarTarefas()

def atualizarStatusTarefa(): # UPDATE
    print()
    conn= DBHelper()
    listarTarefas()
    print()
    id_tarefa = int(input("Digite o número da tarefa que foi concluída: "))
    sql = conn.execute(f"UPDATE ew_todolist SET feito=0 WHERE id={id_tarefa}") 
    print()
    listarTarefas()
   
def deletarTarefa(): # DELETE
    print()
    conn= DBHelper()
    listarTarefas()
    print()
    id_tarefa = int(input("Digite o número da tarefa que deseja deletar: "))
    sql = conn.execute(f"DELETE FROM ew_todolist WHERE id={id_tarefa}") 
    print()
    listarTarefas()

############################################
while True:
    print()
    print("######## TO-DO LIST ########")
    print("1 - Inserir Tarefa") #ok
    print("2 - Listar Tarefas") #ok
    print("3 - Atualizar Tarefa") #ok
    print("4 - Atualizar Status Tarefa") #ok
    print("5 - Deletar Tarefa") #ok
    print("0 - Sair")
    print()
    opcao = input()
    
    match opcao:
        case '0':
            print('Saindo...')
            break
        case '1':
            inserirTarefa()
        case '2':
            listarTarefas()
        case '3':
            atualizarTarefa()
        case '4':
            atualizarStatusTarefa()
        case '5':
            deletarTarefa()
        case _:
            print("Opção inválida!")

 
############################################

