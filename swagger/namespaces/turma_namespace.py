from flask_restx import Namespace, Resource, fields
from Models.turma_model import Turma, adicionar_turma
from swagger import api
from config import db

turmas_ns = Namespace('turmas', description='Operações relacionadas às turmas')

turma_model = api.model('Turma', {
    'id': fields.Integer(description='ID da turma'),
    'descricao': fields.String(description='Descrição da turma', required=True),
    'sala': fields.String(description='Sala da turma', required=True),
    'turno': fields.String(description='Turno da turma', required=True),
})


@turmas_ns.route('/')
class TurmasList(Resource):
    @turmas_ns.marshal_list_with(turma_model)
    def get(self):
        """Lista todas as turmas"""
        turmas = Turma.query.all()
        return [turma.to_dict() for turma in turmas]

    @turmas_ns.expect(turma_model)

    @turmas_ns.doc('adicionar_turma')
    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model, code=201)
    def post(self):
        """Adiciona uma nova turma"""
        return adicionar_turma(turmas_ns.payload)



@turmas_ns.route('/<int:id>')
class TurmaResource(Resource):
    @turmas_ns.marshal_with(turma_model)
    def get(self, id):
        """Busca uma turma pelo ID"""
        turma = Turma.query.get_or_404(id)
        return turma.to_dict()

    @turmas_ns.expect(turma_model)
    @turmas_ns.response(200, 'Turma atualizada com sucesso')
    def put(self, id):
        """Atualiza uma turma"""
        turma = Turma.query.get_or_404(id)
        dados = api.payload

        turma.descricao = dados.get('descricao', turma.descricao)
        turma.sala = dados.get('sala', turma.sala)
        turma.turno = dados.get('turno', turma.turno)

        db.session.commit()
        return turma.to_dict(), 200

    @turmas_ns.response(200, 'Turma deletada com sucesso')
    def delete(self, id):
        """Remove uma turma pelo ID"""
        turma = Turma.query.get_or_404(id)
        db.session.delete(turma)
        db.session.commit()
        return {"mensagem": "Turma deletada com sucesso"}, 200
