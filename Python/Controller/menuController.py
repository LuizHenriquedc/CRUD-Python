from Conexao.conector import *
from Controller.selectAll import usuarios
import time

class MenuController:

    def cadastro(self, opcao):

        cursor = conn.cursor()
        
        if opcao == 1:

            while True:

                while True:

                    nome = input("""
                    \n\tDigite o nome do usuário: """)
                    nome_cap = nome.capitalize()

                    if nome_cap == '' or nome_cap.isalpha() == False:
                        print("""Nome inválido, digite novamente """)
                    
                    else:
                        break
                
                while True:

                    try:
                        idade = input("""
                        \n\tDigite a idade do usuário: """)
                        idade1 = int((idade))
                        break

                    except ValueError:
                        print("""
                        \n\tIdade inválida, digite novamente: """)

                while True:
                    
                    sexo = input("""
                    \n\tDigite o sexo do usuário: """)
                    sexo_cap = sexo.upper()

                    if sexo == '' and sexo.isnumeric() == False:
                        print("""
                        \n\tSexo inválido, digite novamente: """)
                    else:
                        break

                try:
                    sql = f'insert into usuarios (Nome, Idade, Sexo) values ("{nome_cap}", "{idade1}", "{sexo_cap}")'
                    cursor.execute(sql)
                    conn.commit()
                    break

                except error as e:
                    print(e)
        
        if opcao == 2:

            while True:
                identificacao = []

                sql = 'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados para mostrar """)
                    break
                else:
                    usuarios()
                    break

        if opcao == 3:

            while True:
                identificacao = []

                sql = 'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    break

                else:

                    usuarios()
                    try:
                        escolha = int(input("""
                        \n\tDigite o ID do usuário que deseja alterar: """))

                        if escolha not in identificacao:
                            print("""
                        \n\tId inválido""")
                            continue

                        else:
                            pass
                    except ValueError:
                        print("""
                        \n\tId inválido""")
                        continue

                    while True:
                        alterar = input("""
                    \n\tO que você deseja alterar?: """)
                        alterar = alterar.capitalize()
                        
                        if alterar == '':
                            print("""
                    \n\tOpção inválida""")
                            continue

                        elif alterar != 'Nome' and alterar != 'Sexo' and alterar != 'Idade':
                            print("""
                    \n\tOpção inválida""")
                            continue

                        else:
                            break

                    while True:
                        if alterar == 'Nome':
                            nome = input("""
                        \n\tDigite o novo nome: """)
                            nome = nome.capitalize()

                            if nome == '':
                                print("""
                    \n\tNome em branco, digite novamente! """)
                                continue

                            else:
                                pass

                            sql = f'update usuarios set Nome = "{nome}" where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()
                            print("""
                        \n\tUsuário alterado com sucesso""")
                            time.sleep(2)
                            usuarios()
                            break
                        
                        elif alterar == 'Sexo':
                            sexo = input("""
                        \n\tDigite o novo sexo do usuário(M/F): """)
                            sexo = sexo.capitalize()

                            if sexo == '':
                                print("""
                    \n\tSexo em branco, digite novamente! """)
                                continue

                            elif sexo != 'M' and sexo != 'F':
                                print("""
                    \n\tSexo inválido, digite novamente! """)
                                continue

                            else:
                                pass

                            sql = f'update usuarios set Sexo = "{sexo}" where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()
                            print("""
                        \n\tUsuário alterado com sucesso""")
                            time.sleep(2)
                            usuarios()
                            break

                        elif alterar == 'Idade':

                            try:
                                idade = int(input("""
                        \n\tDigite a nova idade do usuário: """))

                                sql = f'update usuarios set Idade = "{idade}" where Id = "{escolha}"'
                                cursor.execute(sql)
                                conn.commit()
                                print("""
                        \n\tUsuário alterado com sucesso""")
                                time.sleep(2)
                                usuarios()
                                break

                            except ValueError:
                                print("""
                        \n\tIdade inválida, tente novamente! """)
                break

        if opcao == 4:

            while True:
                identificacao = []

                sql = 'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    break

                else:

                    try:
                        usuarios()
                        
                        escolha = int(input("""
                        \n\tDigite o ID do usuário que deseja excluir: """))

                        if escolha not in identificacao:
                            print("""
                        \n\tId inválido""")
                            continue

                        else:
                            sql = f'delete from usuarios where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()

                            print("""
                        \n\tUsuário exluido com sucesso""")
                            time.sleep(2)

                            if len(identificacao) == 0:
                                break
                            
                    except ValueError:

                        print("""
                    \n\tID inválido""")
                        continue

                break
        
        if opcao == 5:
            while True:
                identificacao = []

                sql = 'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    limpar = 'truncate usuarios'
                    cursor.execute(limpar)
                    conn.commit()
                    break

                else:
                    sql = 'truncate usuarios'
                    sql2 = 'alter table usuarios auto_increment = 1'
                    cursor.execute(sql)
                    cursor.execute(sql2)
                    conn.commit()

                    print("""
                    \n\tTodos os usuários foram deletados """)
                    break
