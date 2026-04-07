import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.recipes import recipes_bp
from config import Config

def create_app():
    app = Flask(__name__, static_folder='../frontend', static_url_path='')
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(recipes_bp)

    @app.route("/")
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)