from flask_restx import Namespace, Resource, fields
from Models.aluno_model import Aluno
from swagger import api
from config import db
from datetime import datetime

alunos_ns = Namespace(
    'alunos', description='Operações relacionadas aos alunos')

aluno_model = api.model('Aluno', {
    'id': fields.Integer(description='ID do aluno', required=True),
    'nome': fields.String(description='Nome do aluno', required=True),
    'idade': fields.Integer(description='Idade do aluno', required=True),
    'turma_id': fields.Integer(required=True, description='ID da turma'),
    'data_nascimento': fields.Date(description='Data de nascimento do aluno', required=True),
    'nota_primeiro_semestre': fields.Float(description='Nota do primeiro semestre', required=False),
    'nota_segundo_semestre': fields.Float(description='Nota do segundo semestre', required=False),
    'media_final': fields.Float(description='Média final do aluno', required=False)
})


@alunos_ns.route('/')
class AlunosList(Resource):
    @alunos_ns.marshal_list_with(aluno_model)
    def get(self):
        alunos = Aluno.query.all()
       
        return [aluno.to_dict() for aluno in alunos]

    @alunos_ns.expect(aluno_model)
    @alunos_ns.response(201, 'Aluno criado com sucesso')
    def post(self):
        dados = api.payload
        try:
            data_nascimento = datetime.strptime(
                dados['data_nascimento'], '%Y-%m-%d').date()
        except ValueError:
            return {'erro': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400

        novo_aluno = Aluno(
            nome=dados['nome'],
            idade=dados['idade'],
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=dados.get('nota_primeiro_semestre'),
            nota_segundo_semestre=dados.get('nota_segundo_semestre'),
            turma_id=dados.get('turma_id')
        )
        novo_aluno.calcular_media()
        db.session.add(novo_aluno)
        db.session.commit()
        
        return novo_aluno.to_dict(), 201


@alunos_ns.route('/<int:id>')
class AlunoResource(Resource):
    @alunos_ns.marshal_with(aluno_model)
    def get(self, id):
        aluno = Aluno.query.get_or_404(id)
        return aluno.to_dict()  

    @alunos_ns.expect(aluno_model)
    @alunos_ns.response(200, 'Aluno atualizado com sucesso')
    def put(self, id):
        aluno = Aluno.query.get_or_404(id)
        dados = api.payload

        
        aluno.nome = dados.get('nome', aluno.nome)
        aluno.idade = dados.get('idade', aluno.idade)

        if 'data_nascimento' in dados:
            try:
                aluno.data_nascimento = datetime.strptime(
                    dados['data_nascimento'], '%Y-%m-%d').date()
            except ValueError:
                return {'erro': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400

        aluno.nota_primeiro_semestre = dados.get(
            'nota_primeiro_semestre', aluno.nota_primeiro_semestre)
        aluno.nota_segundo_semestre = dados.get(
            'nota_segundo_semestre', aluno.nota_segundo_semestre)
        aluno.turma_id = dados.get('turma_id', aluno.turma_id)

        aluno.calcular_media()
        db.session.commit()

        return aluno.to_dict(), 200
    
    @alunos_ns.doc('deletar_aluno')
    @alunos_ns.response(200, 'Aluno removido com sucesso')

  
    @alunos_ns.response(200, 'Aluno deletado com sucesso')
    @alunos_ns.response(404, 'Aluno não encontrado')
    def delete(self, id):
        aluno = Aluno.query.get(id)  
        if not aluno: 
            return {"erro": "Aluno não encontrado"}, 404
        db.session.delete(aluno)
        db.session.commit()
        return {'mensagem': 'Aluno deletado com sucesso'}, 200
    