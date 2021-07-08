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
    dose = db.Column(db.String(1), nullable = False)

    def __init__(self, name_, idade, estado, sexo, dose):
        self.name_ = name_
        self.idade = idade
        self.estado = estado
        self.sexo = sexo
        self.dose = dose
    
    @staticmethod
    def read_all():
        return Pacientes.query.all()
    
    @staticmethod
    def read_single(pacientes_id):
        return Pacientes.query.get(pacientes_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, new_data):
        self.name_ = new_data.name_
        self.idade = new_data.idade
        self.estado = new_data.estado
        self.sexo = new_data.sexo
        self.dose = new_data.dose
        self.save()

    def delete(self):
        db.session.delete(self) 
        db.session.commit()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/read')
def listar_pacientes():
    pacientes=Pacientes.read_all()
    return render_template('listar_pacientes.html', registros=pacientes)

@bp.route('/read/<pacientes_id>')
def lista_detalhe_paciente(pacientes_id):
    paciente = Pacientes.read_single(pacientes_id)
    return render_template('read_single.html', pacientes=paciente)

@bp.route('/create', methods=('GET','POST'))
def create():
    id_atribuido = None #como o metodo utiliz. no form é POST, pegamos os valores dos campos
    if request.method =='POST':
        form=request.form
        paciente = Pacientes(form['nome'], form['idade'], form['UF'], form['sexo'], form['dose'])
        paciente.save()
        id_atribuido=paciente.id
    return render_template('create.html', id_atribuido=id_atribuido)

@bp.route('/update/<pacientes_id>', methods=('GET','POST'))
def update(pacientes_id):
    sucesso = None
    paciente=Pacientes.read_single(pacientes_id)
    if request.method =='POST':
        form=request.form
        new_data= Pacientes(form['nome'], form['idade'], form['UF'], form['sexo'], form['dose'])
        paciente.update(new_data)
        sucesso = True
    return render_template('update.html', paciente=paciente,sucesso=sucesso)

@bp.route('/delete/<pacientes_id>') #rota de confirmação do delete
def delete(pacientes_id):
    paciente=Pacientes.read_single(pacientes_id)
    return render_template('delete.html', paciente=paciente)

@bp.route('/delete/<pacientes_id>/confirmed') #rota que realiza de fato a deleçõ do filme selecionado e mostra o html de sucesso.
def delete_confirmed(pacientes_id):
    sucesso = None
    paciente=Pacientes.read_single(pacientes_id)

    if paciente:
        paciente.delete()
        sucesso=True
    return render_template('delete.html', sucesso=sucesso)

app.register_blueprint(bp)

if __name__ == 'main':
    app.run(debug=True)


        