class Aula:
    def __init__(self, turma, disciplina, data, horario, sala):
        self.turma = turma
        self.disciplina = disciplina
        self.data = data
        self.horario = horario
        self.sala = sala

    def to_dict(self):
        return {
            "turma": self.turma,
            "disciplina": self.disciplina,
            "data": self.data,
            "horario": self.horario,
            "sala": self.sala
        }


class Aluno:
    def __init__(self, nome, turma, contato):
        self.nome = nome
        self.turma = turma
        self.contato = contato

    def to_dict(self):
        return {
            "nome": self.nome,
            "turma": self.turma,
            "contato": self.contato
        }


class Notificacao:
    def __init__(self, aluno, disciplina, data, horario, sala, status):
        self.aluno = aluno
        self.disciplina = disciplina
        self.data = data
        self.horario = horario
        self.sala = sala
        self.status = status

    def to_dict(self):
        return {
            "aluno": self.aluno,
            "disciplina": self.disciplina,
            "data": self.data,
            "horario": self.horario,
            "sala": self.sala,
            "status": self.status
        }