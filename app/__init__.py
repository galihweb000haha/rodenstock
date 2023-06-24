"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from . import assets, forms, models

from sqlalchemy.orm import declarative_base
Base = declarative_base()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
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
        # db.session.expire_all()
        # db.session.commit()
        
        # Compile static assets
        # if app.config["FLASK_ENV"] == "development":
            # compile_static_assets(app)

        return app


    