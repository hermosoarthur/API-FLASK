from datetime import datetime
from config import db


class ProfessorNaoIdentificado(Exception):
    pass


class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    
    turmas = db.relationship('Turma', backref='professores',
                             lazy=True) 

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
        }


def listar_professores():
    professores = db.session.execute(db.select(Professor)).scalars().all()
    return [
        {
            "id": p.id,
            "nome": p.nome,
            "idade": p.idade,
            "materia": p.materia,
            "observacoes": p.observacoes
        }
        for p in professores
    ]


def buscar_professor_por_id(professor_id):
    professor = db.session.get(Professor, professor_id)
    if not professor:
        return None
    return {
        "id": professor.id,
        "nome": professor.nome,
        "idade": professor.idade,
        "materia": professor.materia,
        "observacoes": professor.observacoes
    }


def adicionar_professor(dados):
    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados.get('observacoes')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return {
        "id": novo_professor.id,
        "nome": novo_professor.nome,
        "idade": novo_professor.idade,
        "materia": novo_professor.materia,
        "observacoes": novo_professor.observacoes
    }, 201


def atualizar_professor(idProfessor, dados):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoIdentificado(
            f"Professor com ID {idProfessor} não encontrado.")

    if 'nome' in dados:
        professor.nome = dados['nome']
    if 'idade' in dados:
        professor.idade = dados['idade']
    if 'materia' in dados:
        professor.materia = dados['materia']
    if 'observacoes' in dados:
        professor.observacoes = dados['observacoes']

    db.session.commit()
    return professor.to_dict(), 200


def deletar_professor(professor_id):
    professor = db.session.get(Professor, professor_id)
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    db.session.delete(professor)
    db.session.commit()
    return {"mensagem": "Professor removido com sucesso"}, 200
