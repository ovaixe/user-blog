from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # app.config['SECRET_KEY'] = 'e7385cfa269c313aade971d6d9512b33'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    # app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = 'owaisbhat996@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'googleowais'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
