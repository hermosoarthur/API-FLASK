from datetime import datetime
from app import app
from Models.professor_model import Professor
from Models.turma_model import Turma
from Models.aluno_model import Aluno
from config import db
import unittest


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.professor_test = Professor(
            nome="Professor Teste",
            idade=45,
            materia="Matemática",
            observacoes="Professor de teste"
        )
        db.session.add(self.professor_test)
        db.session.commit()

        self.turma_test = Turma(
            descricao="Turma Teste",
            professor_id=self.professor_test.id,
            ativo=0,
            observacoes="testes"
        )
        db.session.add(self.turma_test)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # --- Testes Alunos ---

    def test_01_adicionar_aluno(self):
        resposta = self.client.post("/projeto-api-flask/alunos", json={
            "nome": "João Silva",
            "idade": 15,
            "turma_id": self.turma_test.id,
            "data_nascimento": "2010-03-15",
            "nota_primeiro_semestre": 7.5,
            "nota_segundo_semestre": 8.5
        })
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 201)
        self.assertIn("id", data)
        self.assertEqual(data["media_final"], 8.0)

    def test_02_listar_alunos(self):
        resposta = self.client.get("/projeto-api-flask/alunos")
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(data, list)

    def test_03_aluno_inexistente(self):
        resposta = self.client.get("/projeto-api-flask/alunos/9999")
        self.assertEqual(resposta.status_code, 404)

    def test_04_atualizar_aluno(self):
        aluno_resp = self.client.post("/projeto-api-flask/alunos", json={
            "nome": "Carlos Souza",
            "idade": 14,
            "turma_id": self.turma_test.id,
            "data_nascimento": "2011-02-10",
            "nota_primeiro_semestre": 6.0,
            "nota_segundo_semestre": 7.0
        })
        aluno = aluno_resp.get_json()

        resposta = self.client.put(f"/projeto-api-flask/alunos/{aluno['id']}", json={
            "nome": "Carlos Eduardo Souza",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 9.0
        })
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(data["nome"], "Carlos Eduardo Souza")
        self.assertEqual(data["media_final"], 8.5)

    def test_05_deletar_aluno(self):
        aluno_resp = self.client.post("/projeto-api-flask/alunos", json={
            "nome": "Ana Paula",
            "idade": 15,
            "turma_id": self.turma_test.id,
            "data_nascimento": "2010-08-25",
            "nota_primeiro_semestre": 9.5,
            "nota_segundo_semestre": 10.0
        })
        aluno = aluno_resp.get_json()

        resposta = self.client.delete(f"/projeto-api-flask/alunos/{aluno['id']}")
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(data["mensagem"], "Aluno deletado com sucesso")

    # --- Testes Professores ---

    def test_06_adicionar_professor(self):
        resposta = self.client.post('/projeto-api-flask/professores', json={
            "nome": "Maria Santos",
            "idade": 42,
            "materia": "Matemática",
            "observacoes": "Especialista em álgebra linear"
        })
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 201)
        self.assertIn("id", data)

    def test_07_listar_professores(self):
        resposta = self.client.get('/projeto-api-flask/professores')
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(data, list)
        if data:
            self.assertIsInstance(data[0], dict)

    def test_08_professor_inexistente(self):
        resposta = self.client.get('/projeto-api-flask/professores/9999')
        self.assertEqual(resposta.status_code, 404)

    def test_09_atualizar_professor(self):
        resposta = self.client.put(f'/projeto-api-flask/professores/{self.professor_test.id}', json={
            "nome": "Professor Atualizado",
            "idade": 46,
            "materia": "Matemática Avançada"
        })
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(data["nome"], "Professor Atualizado")

    def test_10_deletar_professor(self):
        professor_resp = self.client.post('/projeto-api-flask/professores', json={
            "nome": "Professor para Deletar",
            "idade": 50,
            "materia": "Física",
            "observacoes": "Para teste de deleção"
        })
        professor = professor_resp.get_json()

        resposta = self.client.delete(f'/projeto-api-flask/professores/{professor["id"]}')
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(data["mensagem"], "Professor deletado com sucesso")

    # --- Testes Turmas ---

    def test_11_criar_turma(self):
        resposta = self.client.post("/projeto-api-flask/turmas", json={
            "descricao": "Turma de Química Avançada",
            "professor_id": self.professor_test.id,
            "ativo": 1,
            "observacoes": "Tests"
        })
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 201)
        self.assertIn("id", data)

    def test_12_listar_turmas(self):
        resposta = self.client.get("/projeto-api-flask/turmas")
        self.assertEqual(resposta.status_code, 200)

    def test_13_turma_inexistente(self):
        resposta = self.client.get("/projeto-api-flask/turmas/9999")
        self.assertEqual(resposta.status_code, 404)

    def test_14_atualizar_turma(self):
        resposta = self.client.put(f"/projeto-api-flask/turmas/{self.turma_test.id}", json={
            "descricao": "Turma de Matemática",
            "professor_id": self.professor_test.id,
            "ativo": 0,
            "observacoes": "Teste"
        })
        self.assertEqual(resposta.status_code, 200)

    def test_15_deletar_turma(self):
        turma_resp = self.client.post("/projeto-api-flask/turmas", json={
            "descricao": "Turma Temporária",
            "professor_id": self.professor_test.id,
            "ativo": 1,
            "observacoes": "Testss"
        })
        turma = turma_resp.get_json()

        resposta = self.client.delete(f"/projeto-api-flask/turmas/{turma['id']}")
        data = resposta.get_json()
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(data["mensagem"], "Turma deletada com sucesso")


if __name__ == '__main__':
    unittest.main()
