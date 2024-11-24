from flask import Flask

from .error_handler import err_handler_bp



def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.user_route import user_bp
    from .orders.chat_route import chat_bp
    from .orders.chat_participant_route import chat_participant_bp
    from .orders.user_status_route import user_status_bp
    from .orders.activity_log_route import activity_log_bp
    from .orders.procedure_route import procedure_bp
    from .orders.procedure_route import stats_bp
    from .orders.procedure_route import trigger_bp


    app.register_blueprint(user_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(chat_participant_bp)
    app.register_blueprint(user_status_bp)
    app.register_blueprint(activity_log_bp)
    app.register_blueprint(procedure_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(trigger_bp)