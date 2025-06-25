from flask import Flask
from flask_cors import CORS
from routes.recommend import recommend_bp
from routes.improve import improve_bp
from routes.health_analyzer import health_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# Register API routes
app.register_blueprint(recommend_bp, url_prefix="/api")
app.register_blueprint(improve_bp, url_prefix="/api")
app.register_blueprint(health_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "AI Recipe Recommender API is running"}

if __name__ == "__main__":
    app.run(debug=True)
