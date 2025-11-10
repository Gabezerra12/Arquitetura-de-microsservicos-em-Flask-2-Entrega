from flask import Flask, jsonify
from flasgger import Swagger
from database import init_db
from routes import bp as routes_bp
import os
app = Flask(__name__)
Swagger(app)
db_file = os.environ.get('DB_FILE','atividades.db')
init_db(app, db_file)
app.register_blueprint(routes_bp, url_prefix='/')
@app.route('/')
def index():
    return jsonify({"service":"atividades", "endpoints":["/apidocs","/status"]}), 200
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5002)  # Atividades service on port 5002
