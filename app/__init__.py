"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
# from . import assets, forms, models

from sqlalchemy.orm import declarative_base
Base = declarative_base()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

"""Construct the core app object."""
app = Flask(__name__, instance_relative_config=False)
app.config['WTF_CSRF_ENABLED'] = True

# Konfigurasi Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USERNAME'] = 'galih11120@gmail.com'  
app.config['MAIL_PASSWORD'] = 'rkgsuobqdhwdsypc' 
# rkgsuobqdhwdsypc
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Batasi ke 16 MB


mail = Mail(app)
csrf = CSRFProtect(app)

migrate.init_app(app, db)
app.config.from_object("config.Config")

# Initialize Plugins
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    from . import routes
    from .assets import compile_static_assets

    # Register Blueprints
    app.register_blueprint(routes.main.main_bp)
    app.register_blueprint(routes.auth.auth_bp)
    app.register_blueprint(routes.admin.admin_bp)
    app.register_blueprint(routes.prodi.prodi_bp)
    app.register_blueprint(routes.predict.predict_bp)

    # Create Database Models
    db.create_all()



    