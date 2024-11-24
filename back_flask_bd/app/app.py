import os
from waitress import serve
import yaml
from back_flask_bd.app.my_project import create_app

# Порти та інші налаштування
DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

def load_config():
    # Вказуємо шлях до YAML файлу з конфігурацією
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    # Завантажуємо конфігураційні дані з YAML файлу
    with open(config_yaml_path, 'r', encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
        return config_data_dict

if __name__ == '__main__':
    # Отримуємо середовище (розробка або продакшн)
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    config_data_dict = load_config()
    additional_config = config_data_dict.get(ADDITIONAL_CONFIG)

    # Вибір конфігурації в залежності від середовища
    if flask_env == DEVELOPMENT:
        config_data = config_data_dict.get(DEVELOPMENT)
        if not config_data:
            raise ValueError("Development configuration not found in YAML file.")
        # Створюємо додаток і запускаємо його в режимі розробки
        app = create_app(config_data, additional_config)
        app.run(port=DEVELOPMENT_PORT, debug=True)

    elif flask_env == PRODUCTION:
        config_data = config_data_dict.get(PRODUCTION)
        if not config_data:
            raise ValueError("Production configuration not found in YAML file.")
        # Створюємо додаток і запускаємо його через waitress для продакшн середовища
        app = create_app(config_data, additional_config)
        serve(app, host=HOST, port=PRODUCTION_PORT)

    else:
        raise ValueError("FLASK_ENV must be either 'development' or 'production'")
