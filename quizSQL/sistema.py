from db_helper import DBHelper

""" 
REQUISITOS:
Cadastro de usuário:
    Somente nome do usuário:

Cadastro da pergunta:
    Texto da pergunta.
    Resposta da pergunta (V/F)
        *Fazer 5 perguntas*
    Score (calcular o score e salvar no banco caso seja maior que o score atual)

Funcionalidade de:
-Criar Usuário
-Criar pergunta
-Listar usuários
-Listar perguntas
-Fazer login do usuário
"""




# def CriarTabela():
#     conn = DBHelper()
#     sql = f"CREATE TABLE IF NOT EXISTS ew_quiz_pessoa (id_pessoa INT(9) NOT NULL AUTO_INCREMENT, nome_pessoa VARCHAR(25),score FLOAT, PRIMARY KEY (id_pessoa)"
#     conn.execute(sql)
    
def CriarUsuario():
    conn = DBHelper()
    nome = input("Digite o nome a ser cadastrado: ")
    sql = f"INSERT INTO ew_quiz_pessoa (id_pessoa, nome_pessoa, score) VALUES (Null, '{nome}', 0)"
    conn.execute(sql)

def CriarPergunta():
    conn = DBHelper()
    pergunta = input("Digite o texto da pergunta: ")
    print('##############################')
    print(pergunta)
    while True:
        resposta = input("Digite apenas V para verdadeiro ou F para falso da pergunta registada: ").upper()
        if resposta in 'VF':
            break
        else:
            print("Resposta invalida, use apenas V ou F!")
    sql = f"INSERT INTO ew_quiz_pergunta (pergunta, resposta) VALUES ('{pergunta}','{resposta}')"
    conn.execute(sql)
    
def ListarUsuario():
    conn = DBHelper()
    usuarios = conn.execute("SELECT * FROM ew_quiz_pessoa")
    for user in usuarios:
        print(f"Id: {user[0]} | Nome: {user[1]} | Score: {user[2]}")

def ListarPergunta():
    conn = DBHelper()
    perguntas = conn.execute("SELECT * FROM ew_quiz_pergunta")
    for perg in perguntas:
        print(f"Id: {perg[0]} | Pergunta: {perg[1]} | Resposta: {perg[2]}")


def FazerLogin():
    conn = DBHelper()
    while True:
        usuario = input("Digite seu nome para logar ou 0 (ZERO) para sair: ")
        if usuario == '0':
            break
        sql = conn.execute(f"SELECT * FROM ew_quiz_pessoa WHERE nome_pessoa = '{usuario}' ")
        if usuario != sql[0][1]:
            print("Usuário não localizado!")
        else:
            print(f"Bem vindo {sql[0][1]}")
            print("Vamor jogar!!!!")
            listaTupaPerguntas = conn.execute("SELECT * FROM ew_quiz_pergunta")
            respCertas = 0
            respErrada = 0

            for perg in listaTupaPerguntas:
                print(f"Pergunta nº {perg[0]}")
                print(f"Responda apenas V ou F: \n{perg[1]}  ")
                while True:
                    opcao = input().upper()
                    if opcao in 'VF':
                        break
                    else:
                        print("Resposta invalida, use apenas V ou F!")
                comparacao = opcao == perg[2]
                if comparacao:
                    respCertas += 1
                else:
                    respErrada +=1
            if respCertas == 0:
                print(f"Seu score atual é de: {sql[0][2]}% ")
                print("Vocé não acertou nada!!!!!!!!!!!")
                continue
            if respErrada == 0:
                print(f"Seu score atual é de: {sql[0][2]}% ")
                print("Vocé acertou todas as perguntas, parabéns!")
                print(sql[0][0])
                sql2 = f"UPDATE ew_quiz_pessoa SET score = 100.0 WHERE id_pessoa = {sql[0][0]}"
                #print(sql2)
                conn.execute(sql2)
                novoScore = conn.execute("SELECT * FROM ew_quiz_pessoa")
                conn.execute(novoScore)
                print(f"Score atualizado com sucesso para {novoScore[0][2]} !")
                continue
            balanco = respCertas/respErrada
            print(f"Seu score atual é de: {sql[0][2]}% ")
            if balanco > sql[0][2]:
                sql3 = f"UPDATE ew_quiz_pessoa SET score = {balanco} WHERE id_pessoa = '{sql[0][0]}'"
                conn.execute(sql3)
                print(f"Score atualizado com sucesso para {balanco} !")
            else:
                print("Score não atualizado!")
            
            
    # if alguma copisa in sql




############################################
while True:
    print("##### QUIZ DO MILHÃO #####")
    print("1 - Criar Usuário") #ok
    print("2 - Criar Pergunta") #ok
    print("3 - Listar Usuários") #ok
    print("4 - Listar Pergunta") #ok
    print("5 - Fazer Login")
    print("0 - Sair")
    opcao = input()
    
    match opcao:
        case '0':
            print('Saindo...')
            break
        case '1':
            CriarUsuario()
        case '2':
            CriarPergunta()
        case '3':
            ListarUsuario()
        case '4':
            ListarPergunta()
        case '5':
            FazerLogin()
        case _:
            print("Opção inválida!")
            
############################################


# def InserirNovoLivro():
#     conn = DBHelper()
#     print("Digite o titulo do livro: ")
#     titulo = input()
#     ListarTodasCategorias()
#     print("Digite o ID da categoria")
#     id_categoria = input()
    
#     sql += f"VALUES('{titulo}', '{id_categoria}')"
#     print("Confirmar a operação s/n:")
#     opcao = input()
#     if opcao == "s":
#         conn.execute(sql)
#         print("Livro salvo com sucesso!")
#     else:
#         print("Operação cancelada!")
    
# def AtualizarLivro():
#     conn = DBHelper()
#     ListarTodosLivros()
#     print("Informe o ID do livro a ser editado:")
#     id_livro = input()

#     print("Digite o titulo do livro: ")
#     titulo = input()
#     ListarTodasCategorias()
#     print("Digite o ID da categoria")
#     id_categoria = input()

#     sql = f"UPDATE mf_livros SET titulo='{titulo}', id_categoria='{id_categoria}'"
#     sql += f" WHERE id_livro='{id_livro}'"

#     print("Confirmar a operação s/n:")
#     opcao = input()
#     if opcao == "s":
#         conn.execute(sql)
#         print("Livro salvo com sucesso!")
#     else:
#         print("Operação cancelada!")

# def ListarTodasCategorias():
#     conn = DBHelper()
#     categorias = conn.execute("SELECT * FROM mf_categoria")
#     for categoria in categorias:
#         print(categoria)


# def ListarTodasPessoas():
#     conn = DBHelper()
#     pessoas = conn.execute("SELECT * FROM mf_pessoas")
#     for pessoa in pessoas:
#         print(pessoa)

# def ListarTodosEmprestimos ():
#     conn = DBHelper()
#     sql = "SELECT id_emprestimo, nome, titulo, data_emprestimo"
#     sql += " FROM mf_emprestimos, mf_livros, mf_pessoas"
#     sql += " WHERE mf_emprestimos.id_livro = mf_livros.id_livro"
#     sql += " AND mf_emprestimos.id_pessoa = mf_pessoas.id_pessoa"
#     emprestimos = conn.execute(sql)
#     for emprestimo in emprestimos:
#         print(emprestimo)



