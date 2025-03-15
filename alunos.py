from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

alunos = []
proximo_id = 1  # Simulação de auto incremento

# Media Calculo


def calcular_media(nota1, nota2):
    if nota1 is not None and nota2 is not None:
        return round((nota1 + nota2) / 2, 2)
    return None

# Endpoint todos os alunos


@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

# Endpoint aluno pelo ID


@app.route('/alunos/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = next((a for a in alunos if a['id'] == aluno_id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

# Endpoint adicionar aluno


@app.route('/alunos', methods=['POST'])
def add_aluno():
    global proximo_id
    dados = request.json

    # Validação dos campos obrigatórios
    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    try:
        data_nascimento = datetime.strptime(
            dados['data_nascimento'], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"erro": "Formato de data inválido. Use YYYY-MM-DD."}), 400

    aluno = {
        "id": proximo_id,
        "nome": dados['nome'],
        "idade": dados['idade'],
        "turma_id": dados['turma_id'],
        "data_nascimento": str(data_nascimento),
        "nota_primeiro_semestre": dados.get("nota_primeiro_semestre"),
        "nota_segundo_semestre": dados.get("nota_segundo_semestre"),
        "media_final": calcular_media(dados.get("nota_primeiro_semestre"), dados.get("nota_segundo_semestre"))
    }

    alunos.append(aluno)
    proximo_id += 1
    return jsonify(aluno), 201

# Endpoint atualizar  aluno


@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    dados = request.json
    aluno = next((a for a in alunos if a['id'] == aluno_id), None)

    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    if 'data_nascimento' in dados:
        try:
            dados['data_nascimento'] = str(datetime.strptime(
                dados['data_nascimento'], "%Y-%m-%d").date())
        except ValueError:
            return jsonify({"erro": "Formato de data inválido. Use YYYY-MM-DD."}), 400

    aluno.update({key: dados[key] for key in dados if key in aluno})

    # média final caso as notas sejam alteradas
    aluno["media_final"] = calcular_media(
        aluno.get("nota_primeiro_semestre"), aluno.get("nota_segundo_semestre"))

    return jsonify(aluno)

# Endpoint deletar aluno


@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    global alunos
    alunos = [a for a in alunos if a['id'] != aluno_id]
    return jsonify({"mensagem": "Aluno removido com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
