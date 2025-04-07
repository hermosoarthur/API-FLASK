#alunos_model.py

from datetime import datetime

alunos = []
proximo_id = 1


def calcular_media(n1, n2):
    if n1 is not None and n2 is not None:
        return round((n1 + n2) / 2, 2)
    return None


def validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def listar_alunos():
    return alunos


def buscar_aluno_por_id(aluno_id):
    return next((a for a in alunos if a['id'] == aluno_id), None)


def adicionar_aluno(dados):
    global proximo_id

    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"Campo '{campo}' é obrigatório"}, 400

    data_nascimento = validar_data(dados['data_nascimento'])
    if not data_nascimento:
        return {"erro": "Formato de data inválido. Use YYYY-MM-DD."}, 400

    novo_aluno = {
        "id": proximo_id,
        "nome": dados['nome'],
        "idade": dados['idade'],
        "turma_id": dados['turma_id'],
        "data_nascimento": str(data_nascimento),
        "nota_primeiro_semestre": dados.get("nota_primeiro_semestre"),
        "nota_segundo_semestre": dados.get("nota_segundo_semestre"),
        "media_final": calcular_media(
            dados.get("nota_primeiro_semestre"),
            dados.get("nota_segundo_semestre")
        )
    }

    alunos.append(novo_aluno)
    proximo_id += 1
    return novo_aluno, 201


def atualizar_aluno(aluno_id, dados):
    aluno = buscar_aluno_por_id(aluno_id)
    if not aluno:
        return {"erro": "Aluno não encontrado"}, 404

    if 'data_nascimento' in dados:
        data = validar_data(dados['data_nascimento'])
        if not data:
            return {"erro": "Formato de data inválido. Use YYYY-MM-DD."}, 400
        dados['data_nascimento'] = str(data)

    for chave in dados:
        if chave in aluno:
            aluno[chave] = dados[chave]

    aluno['media_final'] = calcular_media(
        aluno.get("nota_primeiro_semestre"),
        aluno.get("nota_segundo_semestre")
    )
    return aluno, 200


def deletar_aluno(aluno_id):
    global alunos
    alunos = [a for a in alunos if a['id'] != aluno_id]
    return {"mensagem": "Aluno removido com sucesso"}, 200
