from flask import Blueprint, request, jsonify
from Models import professor_model

professor_bp = Blueprint('professor_bp', __name__,
                         url_prefix='/projeto-api-flask/professores')


@professor_bp.route('', methods=['GET'])
def listar_professores():
    return jsonify(professor_model.listar_professores())


@professor_bp.route('', methods=['POST'])
def criar_professor():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    try:
        resultado, status = professor_model.adicionar_professor(dados)
        return jsonify(resultado), status
    except KeyError as e:
        return jsonify({"erro": f"Campo obrigatório faltando: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@professor_bp.route('/<int:professor_id>', methods=['GET'])
def obter_professor(professor_id):
    professor = professor_model.buscar_professor_por_id(professor_id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404


@professor_bp.route('/<int:professor_id>', methods=['PUT'])
def atualizar_professor(professor_id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    resultado, status = professor_model.atualizar_professor(
        professor_id, dados)
    return jsonify(resultado), status


@professor_bp.route('/<int:professor_id>', methods=['DELETE'])
def deletar_professor(professor_id):
    resultado, status = professor_model.deletar_professor(professor_id)
    return jsonify(resultado), status

# Rota para verficar se professor leciona determinada turma


@professor_bp.route('/<int:professor_id>/turma/<int:turma_id>', methods=['GET'])
def verificar_professor_turma(professor_id, turma_id):
    try:
        resultado = professor_model.professor_leciona_turma(
            professor_id, turma_id)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
