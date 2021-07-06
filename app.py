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
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(60), nullable = False)
    password_ = db,Column(db.String(16), nullable = False)

    def __init__(self, user_name, password_):
        self.user_name = user_name
        self.password_ = password_

    @staticmethod
    def read_single(user_name):
        return Users.query.get(user_name)

class Pacientes1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(60), nullable = False)
    idade = db.Column(db.Int, nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    sexo = db.Column(db.String(1), nullable = False)
    imagem_url = db.Column(db.String(255), nullable = False)
    profi = db.Column(db.String(255), nullable = True)

    def __init__(self, name_, idade, estado, sexo, imagem_url, profi):
        self.name_ = name_
        self.idade = idade
        self.estado = estado
        self.sexo = sexo
        self.imagem_url = imagem_url
        self.profi = profi
    
    @staticmethod
    def read_all():
        return Pacientes1.query.order_by(Pacientes1.id.asc()).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

class Pacientes2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(60), nullable = False)
    idade = db.Column(db.Int, nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    sexo = db.Column(db.String(1), nullable = False)
    imagem_url = db.Column(db.String(255), nullable = False)
    profi = db.Column(db.String(255), nullable = True)

    def __init__(self, name_, idade, estado, sexo, imagem_url, profi):
        self.name_ = name_
        self.idade = idade
        self.estado = estado
        self.sexo = sexo
        self.imagem_url = imagem_url
        self.profi = profi
    
    @staticmethod
    def read_all():
        return Pacientes2.query.order_by(Pacientes2.id.asc()).all()

    def save(self):
        db.session.add(self)
        db.session.commit()


        