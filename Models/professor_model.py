professores = []

def listar_professores():
    return professores

def buscar_professor_por_id(prof_id):
    return next((p for p in professores if p['id'] == prof_id), None)

def adicionar_professor(dados):
    campos = {"id", "nome", "idade", "materia", "observacoes"}
    if not campos.issubset(dados.keys()):
        return {"erro": "Campos obrigatórios: id, nome, idade, materia, observacoes"}, 400

    if any(p['id'] == dados['id'] for p in professores):
        return {"erro": "ID já existe"}, 400

    professores.append(dados)
    return {"mensagem": "Professor adicionado com sucesso"}, 201

def atualizar_professor(prof_id, dados):
    professor = buscar_professor_por_id(prof_id)
    if not professor:
        return {"erro": "Professor não encontrado"}, 404

    professor.update(dados)
    return {"mensagem": "Professor atualizado com sucesso"}, 200

def deletar_professor(prof_id):
    global professores
    professores = [p for p in professores if p['id'] != prof_id]
    return {"mensagem": "Professor removido com sucesso"}, 200