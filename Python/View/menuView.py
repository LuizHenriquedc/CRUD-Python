from Model.menuModel import *

class MenuView:

    def menu(self):

        opcao = int
        while opcao != 0:
            try:
                opcao = int(input("""
        1 - Cadastrar usuário 
        2 - Listar usuários
        3 - Editar usuário
        4 - Deletar usuário 
        5 - Excluir todos os usuários
        0 - Sair 
        
        Qual a opção?: """))

                if opcao > 5:
                    print("""
        \n\tOpção inválida! """)
            
                model = MenuModel()
                model.setOpcao(opcao)
                opcao_cadastro = model.cadastro()

            except ValueError as e:
                pass