import unittest
import json
from professores import app  

class TesteProf(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def GetProfessores(self):
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def AddProfessor(self):
        professor_data = {
            "id": 0.1,
            "nome": "CAIO EDUARDO",
            "idade": 27,
            "materia": "Desenvolvimento de API's e Microserviços",
            "Formação": "Bacharelado em Engenharia Mecatrônica"
        }
        response = self.app.post('/professores', json=professor_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("msg", response.json)

    def professorNaoExistente(self):
        response = self.app.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("FALHA", response.json)

    def deleteProfessor(self):
        professor_data = {
            "id": 0.2,
            "nome": "FABIO NOGUEIRA",
            "idade": 40,
            "materia": "Engenharia de Requisitos",
            "Formação": "Graduado em Processamento de Dados"
        }
        self.app.post('/professores', json=professor_data)
        delete_response = self.app.delete('/professores/2')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn("mensagem", delete_response.json)

if __name__ == "__main__":
    unittest.main()
