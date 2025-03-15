import unittest
import json
from professores import app  
class TestProfessorAPI(unittest.TestCase):

    def setUp(self):
        """Configuração inicial para cada teste."""
        app.testing = True
        self.client = app.test_client()
        self.professor = {
            "id": 1,
            "nome": "João Silva",
            "idade": 40,
            "materia": "Matemática",
            "observacoes": "Especialista em álgebra"
        }

    def test_1_add_professor(self):
        """Testa a adição de um professor."""
        response = self.client.post("/professores", json=self.professor)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Professor adicionado com sucesso", response.get_json()["mensagem"])

    def test_2_get_professores(self):
        """Testa a obtenção da lista de professores."""
        response = self.client.get("/professores")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_3_get_professor_por_id(self):
        """Testa a obtenção de um professor específico."""
        self.client.post("/professores", json=self.professor)
        response = self.client.get("/professores/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["nome"], "João Silva")

    def test_4_update_professor(self):
        """Testa a atualização dos dados de um professor."""
        self.client.post("/professores", json=self.professor)
        response = self.client.put("/professores/1", json={"nome": "João Souza"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Professor atualizado com sucesso", response.get_json()["mensagem"])

    def test_5_delete_professor(self):
        """Testa a remoção de um professor."""
        self.client.post("/professores", json=self.professor)
        response = self.client.delete("/professores/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Professor removido com sucesso", response.get_json()["mensagem"])

if __name__ == "__main__":
    unittest.main()
