import os
import configs
from api import create_app

from api.videos.view import videos_bp

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

if ENVIRONMENT == "dev":
    app = create_app(config_class=configs.DevConfig)
else:
    raise ValueError("Invalid environment")

@app.route("/ready")
def ready():
    return "ok"

# Register blueprints
app.register_blueprint(videos_bp)

from db import db

@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)

    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")