from flask import Flask, jsonify
from user_code.handler import handle


app = Flask(__name__)


@app.route("/")
def hello():
    user_code_response = handle()
    responsse = {'response': 'HELLO WROLD! vraceno z userCode: ' + user_code_response}
    return jsonify(responsse)

if __name__ == "__main__":
    print("MOCK API SECOND STARTED")
    app.run(debug=True, host="0.0.0.0", port=5000)
