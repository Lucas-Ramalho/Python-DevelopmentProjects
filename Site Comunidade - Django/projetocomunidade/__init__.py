from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



app.config['SECRET_KEY'] = '7142fdba440755294c6ad7529fd0bd35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto-comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça Login para acessar essa página'
login_manager.login_message_category = 'alert-info'

from projetocomunidade import routes