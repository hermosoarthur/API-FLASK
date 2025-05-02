from flask import Blueprint, request, jsonify
from Models import professor_model

professor_bp = Blueprint('professor_bp', __name__, url_prefix='/professores')

@professor_bp.route('', methods=['GET'])
def listar_professores():
    return jsonify(professor_model.listar_professores())

@professor_bp.route('', methods=['POST'])
def criar_professor():
    dados = request.json
    resultado, status = professor_model.adicionar_professor(dados)
    return jsonify(resultado), status

@professor_bp.route('/<int:prof_id>', methods=['GET'])
def obter_professor(prof_id):
    professor = professor_model.buscar_professor_por_id(prof_id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/<int:prof_id>', methods=['PUT'])
def atualizar_professor(prof_id):
    dados = request.json
    resultado, status = professor_model.atualizar_professor(prof_id, dados)
    return jsonify(resultado), status

@professor_bp.route('/<int:prof_id>', methods=['DELETE'])
def deletar_professor(prof_id):
    resultado, status = professor_model.deletar_professor(prof_id)
    return jsonify(resultado), status