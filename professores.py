from flask import Flask, jsonify, request

app = Flask(__name__)


professores = []


@app.route("/professores", methods=["GET"])
def get_professores():
    return jsonify(professores)


@app.route("/professores", methods=["POST"])
def add_professor():
    data = request.json
    required_fields = {"id", "nome", "idade", "materia", "observação"}
    
    if not required_fields.issubset(data.keys()):
        return jsonify({"erro": "Campos obrigatórios: id, nome, idade, materia, observação"}), 400
    
   
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

if __name__ == "__main__":
    app.run(debug=True)
