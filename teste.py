import unittest
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # --- Testes Alunos ---
    def test_01_adicionar_aluno(self):
        resposta = self.client.post("/alunos", json={
            "nome": "João",
            "idade": 15,
            "turma_id": 1,
            "data_nascimento": "2010-03-15",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 8.0
        })
        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.json["media_final"], 7.5)

    def test_02_listar_alunos(self):
        resposta = self.client.get("/alunos")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json, list)

    def test_03_aluno_inexistente(self):
        resposta = self.client.get("/alunos/999")
        self.assertEqual(resposta.status_code, 404)

    def test_04_atualizar_aluno(self):
        resposta = self.client.put("/alunos/1", json={
            "nome": "Arthur",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 9.0
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json["nome"], "Arthur")
        self.assertEqual(resposta.json["media_final"], 9.0)

    def test_05_deletar_aluno(self):
        resposta = self.client.delete("/alunos/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("mensagem", resposta.json)

    # --- Testes Professores ---
    def test_06_adicionar_professor(self):
        resposta = self.client.post("/professores", json={
            "id": 1,
            "nome": "Maria",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "PHD em álgebra"
        })
        self.assertEqual(resposta.status_code, 201)

    def test_07_listar_professores(self):
        resposta = self.client.get("/professores")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json, list)

    def test_08_professor_inexistente(self):
        resposta = self.client.get("/professores/999")
        self.assertEqual(resposta.status_code, 404)

    def test_09_atualizar_professor(self):
        resposta = self.client.put("/professores/1", json={
            "nome": "Marina",
            "idade": 41
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("mensagem", resposta.json)

    def test_10_deletar_professor(self):
        resposta = self.client.delete("/professores/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("mensagem", resposta.json)

    # --- Testes Turmas ---
    def test_11_criar_turma(self):
        resposta = self.client.post("/turmas", json={
            "id": 1,
            "descricao": "Turma de Química",
            "professor_id": 1,
            "ativo": True
        })
        self.assertEqual(resposta.status_code, 201)

    def test_12_listar_turmas(self):
        resposta = self.client.get("/turmas")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json, list)

    def test_13_turma_inexistente(self):
        resposta = self.client.get("/turmas/999")
        self.assertEqual(resposta.status_code, 404)

    def test_14_atualizar_turma(self):
        resposta = self.client.put("/turmas/1", json={
            "descricao": "Turma de Inglês",
            "ativo": False
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json["descricao"], "Turma de Inglês")

    def test_15_deletar_turma(self):
        resposta = self.client.delete("/turmas/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("mensagem", resposta.json)


if __name__ == '__main__':
    unittest.main()
