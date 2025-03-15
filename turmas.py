from flask import Flask, jsonify, request

app = Flask(__name__)

turmas = []

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
