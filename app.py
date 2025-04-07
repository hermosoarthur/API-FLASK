from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


professores = []
turmas = []
proximo_id_aluno = 1


def calcular_media(nota1, nota2):
    if nota1 is not None and nota2 is not None:
        return round((nota1 + nota2) / 2, 2)
    return None


# --- PROFESSORES ---


@app.route("/professores", methods=["GET"])
def get_professores():
    return jsonify(professores)


@app.route("/professores", methods=["POST"])
def add_professor():
    data = request.json
    required_fields = {"id", "nome", "idade", "materia", "observacoes"}
    if not required_fields.issubset(data.keys()):
        return jsonify({"erro": "Campos obrigatórios: id, nome, idade, materia, observacoes"}), 400
    if any(prof["id"] == data["id"] for prof in professores):
        return jsonify({"erro": "ID já existe"}), 400
    professores.append(data)
    return jsonify({"mensagem": "Professor adicionado com sucesso"}), 201


@app.route("/professores/<int:id>", methods=["GET"])
def get_professor(id):
    professor = next((prof for prof in professores if prof["id"] == id), None)
    if professor is None:
        return jsonify({"erro": "Professor não encontrado"}), 404
    return jsonify(professor)


@app.route("/professores/<int:id>", methods=["PUT"])
def update_professor(id):
    data = request.json
    for professor in professores:
        if professor["id"] == id:
            professor.update(data)
            return jsonify({"mensagem": "Professor atualizado com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404


@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    global professores
    professores = [prof for prof in professores if prof["id"] != id]
    return jsonify({"mensagem": "Professor removido com sucesso"})

# --- TURMAS ---


@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas), 200


@app.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    if 'id' not in dados or 'descricao' not in dados or 'professor_id' not in dados or 'ativo' not in dados:
        return jsonify({"erro": "Campos 'id', 'descricao', 'professor_id' e 'ativo' são obrigatórios"}), 400
    turmas.append(dados)
    return jsonify(dados), 201


@app.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404
    return jsonify(turma), 200


@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    dados = request.json
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404
    turma.update(dados)
    return jsonify(turma), 200


@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"mensagem": "Turma deletada com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)
