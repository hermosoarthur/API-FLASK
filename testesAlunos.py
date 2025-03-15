import unittest
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


if __name__ == '__main__':
    unittest.main()
