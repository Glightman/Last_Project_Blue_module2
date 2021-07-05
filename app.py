#AQUI NÓS IMPORTAMOS TODAS AS BIBLIOTECAS QUE VAMOS PRCISAR DURANTE O DESENVOLVIMENTO DO NOSSO PROJETO
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


