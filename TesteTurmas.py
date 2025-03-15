import unittest
import json
from turmas import app

class TestTurmaAPI(unittest.TestCase):

    def setUp(self):
        """Configuração inicial para cada teste."""
        app.testing = True
        self.client = app.test_client()
        self.turma = {
            "id": 1,
            "descricao": "Turma de Matemática",
            "professor_id": 1,
            "ativo": True
        }

    def test_1_add_turma(self):
        """Testa a adição de uma turma."""
        response = self.client.post("/turmas", json=self.turma)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["id"], 1)
        self.assertEqual(response.get_json()["descricao"], "Turma de Matemática")

    def test_2_get_turmas(self):
        """Testa a obtenção da lista de turmas."""
        self.client.post("/turmas", json=self.turma)
        response = self.client.get("/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_3_get_turma_por_id(self):
        """Testa a obtenção de uma turma específica."""
        self.client.post("/turmas", json=self.turma)
        response = self.client.get("/turmas/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["descricao"], "Turma de Matemática")

    def test_4_update_turma(self):
        """Testa a atualização dos dados de uma turma."""
        self.client.post("/turmas", json=self.turma)
        response = self.client.put("/turmas/1", json={"descricao": "Turma de Física"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["descricao"], "Turma de Física")

    def test_5_delete_turma(self):
        """Testa a remoção de uma turma."""
        self.client.post("/turmas", json=self.turma)
        response = self.client.delete("/turmas/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Turma deletada com sucesso", response.get_json()["mensagem"])

if __name__ == "__main__":
    unittest.main()