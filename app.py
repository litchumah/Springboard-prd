from flask import Flask
from routes.bert_route import bert

app = Flask(__name__)

app.register_blueprint(bert)

app.run(host='0.0.0.0', port=9000, debug=True)