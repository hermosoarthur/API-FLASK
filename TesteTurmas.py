import unittest
import json
from turmas import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_turmas(self):
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_turma(self):
        turma_data = {
            "id": 1,
            "descricao": "Turma de Medicina",
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
            "descricao": "Turma de Medicina Veterinaria",
            "professor_id": 2,
            "ativo": True
        }
        self.app.post('/turmas', json=turma_data)
        delete_response = self.app.delete('/turmas/2')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("mensagem", delete_response.json)

if __name__ == "__main__":
    unittest.main()
