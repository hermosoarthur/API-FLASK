from flask import Blueprint, request, jsonify
from Models import turma_model

turma_bp = Blueprint('turma_bp', __name__,
                     url_prefix='/projeto-api-flask/turmas')


@turma_bp.route('', methods=['GET'])
def listar_turmas():
    return jsonify(turma_model.listar_turmas())


@turma_bp.route('', methods=['POST'])
def criar_turma():
    dados = request.json
    resultado, status = turma_model.adicionar_turma(dados)
    return jsonify(resultado), status


@turma_bp.route('/<int:turma_id>', methods=['GET'])
def obter_turma(turma_id):
    turma = turma_model.buscar_turma_por_id(turma_id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404


@turma_bp.route('/<int:turma_id>', methods=['PUT'])
def atualizar_turma(turma_id):
    dados = request.json
    resultado, status = turma_model.atualizar_turma(turma_id, dados)
    return jsonify(resultado), status


@turma_bp.route('/<int:turma_id>', methods=['DELETE'])
def deletar_turma(turma_id):
    resultado, status = turma_model.deletar_turma(turma_id)
    return jsonify(resultado), status


