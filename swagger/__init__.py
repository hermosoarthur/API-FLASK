from flask_restx import Api


api = Api(
    version="1.0",
    title="API para gestão escolar",
    description="Api para gestão escolar para alunos, professores e turma!",
    doc="/docs",
    mask_swagger=False,  
    prefix="/projeto-api-flask"
)