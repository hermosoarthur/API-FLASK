from config import db


class TurmaNaoIdentificada(Exception):
    pass


class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean,default=True, nullable=False)
    observacoes = db.Column(db.String(100), nullable=False)

    alunos = db.relationship('Aluno', backref='turma',
                             lazy=True)  

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo,
            'observacoes': self.observacoes
        }


def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas], 200


def buscar_turma_por_id(idTurma):
    turma = db.session.get(Turma, idTurma)
    return turma.to_dict() if turma else None


def adicionar_turma(dados):
    nova_turma = Turma(
        descricao=dados['descricao'],  
        professor_id=dados['professor_id'],
        ativo=dados['ativo'],
        observacoes=dados['observacoes']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return nova_turma.to_dict(), 201

def atualizar_turma(idTurma, dados):
    turma = db.session.get(Turma, idTurma)
    if not turma:
        raise TurmaNaoIdentificada(f"Turma com ID {idTurma} não encontrada.")

    if 'descricao' in dados:
        turma.descricao = dados['descricao']
    if 'professor_id' in dados:
        turma.professor_id = dados['professor_id']
    if 'ativo' in dados:
        turma.ativo = dados['ativo']
    if 'observacoes' in dados:
        turma.observacoes =dados ['observacoes']

    db.session.commit()
    return turma.to_dict(), 200



def deletar_turma(idTurma):
    turma = db.session.get(Turma, idTurma)
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    db.session.delete(turma)
    db.session.commit()
    return {"mensagem": "Turma deletada com sucesso"}, 200


