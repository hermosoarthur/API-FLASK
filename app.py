from flask import Flask
from config import Config

from Controllers.aluno_controller import aluno_bp
from Controllers.professor_controller import professor_bp
from Controllers.turma_controller import turma_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(aluno_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)

if __name__ == '__main__':
    app.run(debug=True)
