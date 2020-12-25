"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    # Application Configuration
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from application.views.base import baseBP
        from application.views.lottery import lotteryBP
        from application.views.password import passwdBP
        from application.minty.views.admin import mintyBP
        
        # Register Blueprints
        app.register_blueprint(baseBP)
        app.register_blueprint(lotteryBP)
        app.register_blueprint(passwdBP)
        app.register_blueprint(mintyBP)
        return app
