from config import db


class TurmaNaoIdentificada(Exception):
    pass


class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    sala = db.Column(db.String(10), nullable=False)
    turno = db.Column(db.String(20), nullable=False)

    alunos = db.relationship('Aluno', backref='turma',
                             lazy=True)  # Relacionamento reverso

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'sala': self.sala,
            'turno': self.turno
        }


def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas], 200


def buscar_turma_por_id(turma_id):
    turma = Turma.query.get(turma_id)
    return turma.to_dict() if turma else None


def adicionar_turma(dados):
    nova_turma = Turma(
        descricao=dados['descricao'],  # Corrigido de 'nome'
        sala=dados['sala'],
        turno=dados['turno']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return nova_turma.to_dict(), 201


def atualizar_turma(idTurma, dados):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmaNaoIdentificada(f"Turma com ID {idTurma} não encontrada.")

    if 'descricao' in dados:
        turma.descricao = dados['descricao']
    if 'professor_id' in dados:
        turma.professor_id = dados['professor_id']
    if 'ativo' in dados:
        turma.ativo = dados['ativo']

    db.session.commit()
    return turma.to_dict(), 200


def deletar_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    db.session.delete(turma)
    db.session.commit()
    return {"mensagem": "Turma deletada com sucesso"}, 200
