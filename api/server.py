import os
import configs
from api import create_app

from api.videos import videos_bp

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

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")