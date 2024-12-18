from flask import Flask
from routes import library_routes

app = Flask(__name__)
app.register_blueprint(library_routes)

if __name__ == "__main__":
    app.run(debug=True)
