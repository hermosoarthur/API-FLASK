from datetime import datetime
from config import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento.strftime("%Y-%m-%d"),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

    def calcular_media(self):
        if self.nota_primeiro_semestre is not None and self.nota_segundo_semestre is not None:
            self.media_final = round(
                (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2, 2)
        else:
            self.media_final = None

def listar_alunos():
    return [aluno.to_dict() for aluno in Aluno.query.all()]

def buscar_aluno_por_id(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    return aluno.to_dict() if aluno else None

def adicionar_aluno(dados):
    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"Campo '{campo}' é obrigatório"}, 400
    try:
        data_nasc = datetime.strptime(dados['data_nascimento'], "%Y-%m-%d").date()
    except ValueError:
        return {"erro": "Formato de data inválido. Use YYYY-MM-DD."}, 400

    novo_aluno = Aluno(
        nome=dados["nome"],
        idade=dados["idade"],
        turma_id=dados["turma_id"],
        data_nascimento=data_nasc,
        nota_primeiro_semestre=dados.get("nota_primeiro_semestre"),
        nota_segundo_semestre=dados.get("nota_segundo_semestre"),
    )
    novo_aluno.calcular_media()

    db.session.add(novo_aluno)
    db.session.commit()

    return novo_aluno.to_dict(), 201

def atualizar_aluno(aluno_id, dados):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {"erro": "Aluno não encontrado"}, 404

    if "nome" in dados:
        aluno.nome = dados["nome"]
    if "idade" in dados:
        aluno.idade = dados["idade"]
    if "turma_id" in dados:
        aluno.turma_id = dados["turma_id"]
    if "data_nascimento" in dados:
        try:
            aluno.data_nascimento = datetime.strptime(dados["data_nascimento"], "%Y-%m-%d").date()
        except ValueError:
            return {"erro": "Formato de data inválido. Use YYYY-MM-DD."}, 400
    if "nota_primeiro_semestre" in dados:
        aluno.nota_primeiro_semestre = dados["nota_primeiro_semestre"]
    if "nota_segundo_semestre" in dados:
        aluno.nota_segundo_semestre = dados["nota_segundo_semestre"]

    aluno.calcular_media()

    db.session.commit()

    return aluno.to_dict(), 200

def deletar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {"erro": "Aluno não encontrado"}, 404

    db.session.delete(aluno)
    db.session.commit()

    return {"mensagem": "Aluno removido com sucesso"}, 200
