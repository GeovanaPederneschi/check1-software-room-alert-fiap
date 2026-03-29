from src.models import Aula, Aluno, Notificacao
from src.repository import carregar_json, salvar_json
from src.utils import validar_data


def listar_aulas_do_dia(data):
    if not validar_data(data):
        print("Data inválida.")
        return []

    aulas_dict = carregar_json("aulas.json")
    aulas = [Aula(**aula) for aula in aulas_dict if aula["data"] == data]

    if not aulas:
        print("Nenhuma aula encontrada para essa data.")
        return []

    print("\nAulas do dia:")
    for aula in aulas:
        print(f"{aula.horario} - {aula.disciplina} ({aula.turma}) - Sala {aula.sala}")

    return aulas


def atualizar_sala(turma, disciplina, data, nova_sala):
    aulas = carregar_json("aulas.json")
    alterado = False

    for aula in aulas:
        if (
            aula["turma"].lower() == turma.lower()
            and aula["disciplina"].lower() == disciplina.lower()
            and aula["data"] == data
        ):
            aula["sala"] = nova_sala
            alterado = True
            break

    if alterado:
        salvar_json("aulas.json", aulas)
        print("Sala atualizada com sucesso.")
    else:
        print("Aula não encontrada.")


def notificar_alunos(data):
    if not validar_data(data):
        print("Data inválida.")
        return

    aulas = carregar_json("aulas.json")
    alunos = carregar_json("alunos.json")
    historico = carregar_json("historico_notificacoes.json")

    aulas_do_dia = [a for a in aulas if a["data"] == data]

    if not aulas_do_dia:
        print("Nenhuma aula cadastrada para esta data.")
        return

    for aula in aulas_do_dia:
        alunos_turma = [aluno for aluno in alunos if aluno["turma"] == aula["turma"]]

        for aluno in alunos_turma:
            mensagem = (
                f"Olá, {aluno['nome']}! Hoje você tem {aula['disciplina']} "
                f"às {aula['horario']} na sala {aula['sala']}."
            )
            print("Notificação enviada:", mensagem)

            notificacao = Notificacao(
                aluno=aluno["nome"],
                disciplina=aula["disciplina"],
                data=aula["data"],
                horario=aula["horario"],
                sala=aula["sala"],
                status="Enviada"
            )

            historico.append(notificacao.to_dict())

    salvar_json("historico_notificacoes.json", historico)
    print("Processo de notificação finalizado.")


def ver_historico():
    historico = carregar_json("historico_notificacoes.json")

    if not historico:
        print("Nenhuma notificação registrada.")
        return

    print("\nHistórico de notificações:")
    for item in historico:
        print(
            f"{item['aluno']} - {item['disciplina']} - {item['data']} "
            f"{item['horario']} - Sala {item['sala']} - {item['status']}"
        )