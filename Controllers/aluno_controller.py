from flask import Blueprint, request, jsonify
from Models import aluno_model
from config import db
from Models.turma_model import Turma  


aluno_bp = Blueprint('aluno_bp', __name__, url_prefix='/projeto-api-flask/alunos')


@aluno_bp.route('', methods=['GET'])
def listar_alunos():
    return jsonify(aluno_model.listar_alunos())


@aluno_bp.route('/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):
    aluno = aluno_model.buscar_aluno_por_id(aluno_id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404


@aluno_bp.route('', methods=['POST'])
def criar_aluno():
    dados = request.json

    
    turma = Turma.query.get(dados.get('turma_id'))
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    
    resultado, status = aluno_model.adicionar_aluno(dados)
    return jsonify(resultado), status


@aluno_bp.route('/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    dados = request.json
    resultado, status = aluno_model.atualizar_aluno(aluno_id, dados)
    return jsonify(resultado), status


@aluno_bp.route('/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    resultado, status = aluno_model.deletar_aluno(aluno_id)
    return jsonify(resultado), status
