from flask_restx import Namespace, Resource, fields
from Models.professor_model import Professor
from config import db
from Models.professor_model import (
    listar_professores,
    buscar_professor_por_id,
    adicionar_professor,
    atualizar_professor,
    deletar_professor
)

professor_ns = Namespace('professores', description='Operações relacionadas a professores')

professor_model = professor_ns.model('Professor', {
    'id': fields.Integer(readonly=True, description='ID do professor'),
    'nome': fields.String(required=True, description='Nome do professor'),
    'idade': fields.Integer(required=True, description='Idade do professor'),
    'materia': fields.String(required=True, description='Matéria ministrada'),
    'observacoes': fields.String(required=False, description='Observações adicionais')
})


@professor_ns.route('/')
class ProfessorList(Resource):
    @professor_ns.doc('listar_professores')
    @professor_ns.marshal_list_with(professor_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @professor_ns.doc('adicionar_professor')
    @professor_ns.expect(professor_model, validate=True)
    @professor_ns.marshal_with(professor_model, code=201)
    def post(self):
        """Adiciona um novo professor"""
        return adicionar_professor(professor_ns.payload)


@professor_ns.route('/<int:id>')
@professor_ns.param('professor_id', 'O identificador do professor')
class ProfessorResource(Resource):
    @professor_ns.doc('buscar_professor')
    @professor_ns.marshal_with(professor_model)
    def get(self, id):
        """Busca um professor pelo ID"""
        professor = buscar_professor_por_id(id)
        if professor:
            return professor
        professor_ns.abort(404, "Professor não encontrado")

    @professor_ns.doc('atualizar_professor')
    @professor_ns.expect(professor_model, validate=True)
    @professor_ns.marshal_with(professor_model)
    def put(self, id):
        """Atualiza os dados de um professor"""
        return atualizar_professor(id, professor_ns.payload)
    

    @professor_ns.doc('deletar_professor')
    @professor_ns.response(404, 'Professor não encontrado')
    @professor_ns.response(200, 'Professor deletado com sucesso')
    def delete(self, id):
        """Remove uma turma pelo ID"""
        professor = Professor.query.get(id)
        if not professor:
            return {"erro": "Professor não encontrado"}, 404
        
        db.session.delete(professor)
        db.session.commit()
        return {"mensagem": "Professor deletado com sucesso"}, 200
  