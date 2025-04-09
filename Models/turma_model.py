turmas = []

def listar_turmas():
    return turmas

def buscar_turma_por_id(turma_id):
    return next((t for t in turmas if t['id'] == turma_id), None)

def adicionar_turma(dados):
    obrigatorios = {'id', 'descricao', 'professor_id', 'ativo'}
    if not obrigatorios.issubset(dados.keys()):
        return {"erro": "Campos 'id', 'descricao', 'professor_id' e 'ativo' são obrigatórios"}, 400

    turmas.append(dados)
    return dados, 201

def atualizar_turma(turma_id, dados):
    turma = buscar_turma_por_id(turma_id)
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    turma.update(dados)
    return turma, 200

def deletar_turma(turma_id):
    global turmas
    turmas = [t for t in turmas if t['id'] != turma_id]
    return {"mensagem": "Turma deletada com sucesso"}, 200