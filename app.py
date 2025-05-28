from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from config import db
from Models import aluno_model, professor_model, turma_model
from Controllers.aluno_controller import aluno_bp
from Controllers.professor_controller import professor_bp
from Controllers.turma_controller import turma_bp
from flask_restx import Api
from swagger.swagger_config import create_swagger
import os
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    if not os.path.exists('banco.db'):
        db.create_all()

create_swagger(app)

app.register_blueprint(aluno_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
