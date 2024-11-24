import os
from typing import Dict, Any
from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import inspect
from sqlalchemy_utils import database_exists, create_database

from back_flask_bd.app.my_project.auth.route import register_routes
from back_flask_bd.app.my_project.database import db
from back_flask_bd.app.my_project.auth.route.orders.user_route import user_bp
from back_flask_bd.app.my_project.auth.route.orders.user_status_route import user_status_bp

# Константи для налаштувань
SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

def create_app(config_data: Dict[str, Any] = None, additional_config: Dict[str, Any] = None) -> Flask:
    app = Flask(__name__)

    register_routes(app)
    # Додаємо налаштування конфігурації, якщо вони передані
    if config_data:
        app.config.update(config_data)
    if additional_config:
        _process_input_config(app.config, additional_config)

    # Конфігурація підключення до бази даних за замовчуванням, якщо URI не вказаний
    app.config.setdefault(
        'SQLALCHEMY_DATABASE_URI', 'mysql://root:password@localhost/newww'
    )
    migrate = Migrate(app, db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.setdefault('SECRET_KEY', os.urandom(24))

    # Ініціалізація бази даних
    db.init_app(app)

    # Тестуємо підключення
    with app.app_context():
        try:
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Список таблиць у базі даних: {tables}")
        except Exception as e:
            print(f"Помилка підключення до бази даних: {e}")

    return app

def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    # Отримуємо значення користувача та пароля з додаткової конфігурації
    root_user = additional_config.get(MYSQL_ROOT_USER)
    root_password = additional_config.get(MYSQL_ROOT_PASSWORD)

    if root_user and root_password:
        # Замінюємо параметри у SQLALCHEMY_DATABASE_URI
        if SQLALCHEMY_DATABASE_URI in app_config:
            app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(
                root_user=root_user, root_password=root_password
            )
    else:
        raise ValueError("MYSQL_ROOT_USER and MYSQL_ROOT_PASSWORD must be provided in additional_config.")

def _init_db(app: Flask) -> None:
    db.init_app(app)
    db_uri = app.config.get("SQLALCHEMY_DATABASE_URI")
    if db_uri and not database_exists(db_uri):
        create_database(db_uri)
    import back_flask_bd.app.my_project.auth.domain  # Імпортуємо домени перед створенням таблиць
    with app.app_context():
        db.create_all()
