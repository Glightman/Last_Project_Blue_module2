#AQUI NÓS IMPORTAMOS TODAS AS BIBLIOTECAS QUE VAMOS PRCISAR DURANTE O DESENVOLVIMENTO DO NOSSO PROJETO
from os import name
from flask import (Flask, Blueprint, render_template, request)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)

""" ABAIXO NÓS COMEÇAMOS A PASSAR OS PARÂMETROS NECESSÁRIOS PARA QUE O PYTHON 
CONSIGA SE CONECTAR COM O BANCO DE DADOS """
user = 'mowcdfac' #ESSA LINHA E A DE BAIXO, REFERE-SE AO NOME DO BANCO DE DADOS QUE TAMBÉM ENCONTRANOS NO SITE DO ELEFANT SQL
database = 'mowcdfac'
password = 'oFnD9oH8EoqbGuk7DF61uq_wAnaFnNTx' #AQUI INSERIMOS A SENHA DO BANCO DE DADOS QUE TAMBÉM ENCONTRAMOS NO ELEFANTE SQL
host = 'tuffi.db.elephantsql.com' #host É O URL DO SERVIDOR ENCONTRADO LA NO BD

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'
db = SQLAlchemy(app)

#MODELO
class Pacientes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(60), nullable = False)
    idade = db.Column(db.String(2), nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    sexo = db.Column(db.String(1), nullable = False)
    imagem_url = db.Column(db.String(255), nullable = False)
    dose = db.Column(db.String(1), nullable = False)

    def __init__(self, name_, idade, estado, sexo, imagem_url, dose):
        self.name_ = name_
        self.idade = idade
        self.estado = estado
        self.sexo = sexo
        self.imagem_url = imagem_url
        self.dose = dose
    
    @staticmethod
    def read_all():
        return Pacientes.query.order_by(Pacientes.id.asc()).all()
    
    @staticmethod
    def read_single(filmes_id):
        return Pacientes.query.get(filmes_id)

    def save(self):
        db.session.add(self)
        db.session.commit()


@bp.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(bp)

if __name__ == 'main':
    app.run(debug=True)


        