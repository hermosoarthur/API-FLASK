import unittest
import json
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_alunos(self):
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_aluno(self):
        aluno_data = {
            "nome": "João Silva",
            "idade": 20,
            "turma_id": 1,
            "data_nascimento": "2004-05-10",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.0
        }
        response = self.app.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_get_aluno_nao_existente(self):
        response = self.app.get('/alunos/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json)

    def test_add_aluno_campos_faltando(self):
        aluno_data = {"nome": "Carlos"}
        response = self.app.post('/alunos', json=aluno_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json)

    def test_delete_aluno(self):
        aluno_data = {
            "nome": "Maria Souza",
            "idade": 21,
            "turma_id": 2,
            "data_nascimento": "2003-08-15"
        }
        response = self.app.post('/alunos', json=aluno_data)
        aluno_id = response.json["id"]
        delete_response = self.app.delete(f'/alunos/{aluno_id}')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("mensagem", delete_response.json)

    # Professores
    def test_get_professores(self):
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_professor(self):
        professor_data = {
            "id": 1,
            "nome": "Ana Costa",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Doutora em Educação"
        }
        response = self.app.post('/professores', json=professor_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("mensagem", response.json)

    def test_get_professor_nao_existente(self):
        response = self.app.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json)

    def test_delete_professor(self):
        professor_data = {
            "id": 2,
            "nome": "Carlos Lima",
            "idade": 50,
            "materia": "História",
            "observacoes": "Especialista em História Medieval"
        }
        self.app.post('/professores', json=professor_data)
        delete_response = self.app.delete('/professores/2')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("mensagem", delete_response.json)

    # Turmas
    def test_get_turmas(self):
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_turma(self):
        turma_data = {
            "id": 1,
            "descricao": "Turma de Física Avançada",
            "professor_id": 1,
            "ativo": True
        }
        response = self.app.post('/turmas', json=turma_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_get_turma_nao_existente(self):
        response = self.app.get('/turmas/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.json)

    def test_delete_turma(self):
        turma_data = {
            "id": 2,
            "descricao": "Turma de Química",
            "professor_id": 2,
            "ativo": True
        }
        self.app.post('/turmas', json=turma_data)
        delete_response = self.app.delete('/turmas/2')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("mensagem", delete_response.json)


if __name__ == "__main__":
    unittest.main()
