from . import api
from swagger.namespaces.aluno_namespace import alunos_ns
from swagger.namespaces.turma_namespace import turmas_ns
from swagger.namespaces.professor_namespace import professor_ns


def create_swagger(app):
    
    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(turmas_ns, path="/turmas")
    api.add_namespace(professor_ns, path="/professores")
    
    api.mask_swagger = False
    