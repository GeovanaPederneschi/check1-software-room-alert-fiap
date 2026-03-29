from src.services import listar_aulas_do_dia, atualizar_sala, notificar_alunos, ver_historico


def iniciar_menu():
    while True:
        print("\n=== SISTEMA DE NOTIFICAÇÃO DE SALA ===")
        print("1. Listar aulas do dia")
        print("2. Atualizar sala")
        print("3. Notificar alunos")
        print("4. Ver histórico de notificações")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            data = input("Digite a data (dd/mm/aaaa): ")
            listar_aulas_do_dia(data)

        elif opcao == "2":
            turma = input("Turma: ")
            disciplina = input("Disciplina: ")
            data = input("Data (dd/mm/aaaa): ")
            nova_sala = input("Nova sala: ")
            atualizar_sala(turma, disciplina, data, nova_sala)

        elif opcao == "3":
            data = input("Digite a data (dd/mm/aaaa): ")
            notificar_alunos(data)

        elif opcao == "4":
            ver_historico()

        elif opcao == "0":
            print("Encerrando sistema.")
            break

        else:
            print("Opção inválida.")