from flask_restx import Namespace, Resource, fields
from swagger import api
from config import db
from Models.turma_model import (
    listar_turmas,
    buscar_turma_por_id,
    adicionar_turma,
    atualizar_turma,
    deletar_turma
)

turmas_ns = Namespace('turmas', description='Operações relacionadas a turmas')

turma_model = api.model('Turma', {
    'id': fields.Integer(description='ID da turma'),
    'nome': fields.String(description='Nome da turma'),
    'sala': fields.String(description='Sala da turma'),
    'turno': fields.String(description='Turno da turma')
})


@turmas_ns.route('/')
class TurmaList(Resource):
    @turmas_ns.doc('listar_turmas')
    @turmas_ns.marshal_list_with(turma_model)
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()

    @turmas_ns.doc('adicionar_turma')
    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model, code=201)
    def post(self):
        """Adiciona uma nova turma"""
        return adicionar_turma(turmas_ns.payload)


@turmas_ns.route('/<int:turma_id>')
@turmas_ns.param('turma_id', 'O identificador da turma')
class TurmaResource(Resource):
    @turmas_ns.doc('buscar_turma')
    @turmas_ns.marshal_with(turma_model)
    def get(self, turma_id):
        """Busca uma turma pelo ID"""
        turma = buscar_turma_por_id(turma_id)
        if turma:
            return turma
        turmas_ns.abort(404, "Turma não encontrada")

    @turmas_ns.doc('atualizar_turma')
    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model)
    def put(self, turma_id):
        """Atualiza uma turma existente"""
        return atualizar_turma(turma_id, turmas_ns.payload)

    @turmas_ns.doc('deletar_turma')
    def delete(self, turma_id):
        """Remove uma turma pelo ID"""
        return deletar_turma(turma_id)
