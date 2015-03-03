from urllib.parse import unquote as urldecode
from flask import Flask, request, make_response
import evaluator

app = Flask(__name__)

@app.route("/")
def evaluate():
    code = urldecode(request.query_string)

    result = evaluator.run(code)
    if not result.strip():
        result = '(no output)'
    
    return make_response(result, 200, {'Content-Type': 'text/plain'})

if __name__ == "__main__":
    app.run(debug=True)
