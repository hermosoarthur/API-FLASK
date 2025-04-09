from flask import Flask
from config import Config

from Controllers.aluno_controller import aluno_bp


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(aluno_bp)

if __name__ == '__main__':
    app.run(debug=True)
