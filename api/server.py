import os
import configs
from api import create_app

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

if ENVIRONMENT == "dev":
    app = create_app(config_class=configs.DevConfig)
else:
    raise ValueError("Invalid environment")

@app.route("/ready")
def ready():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")