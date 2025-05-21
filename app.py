
from flask import Flask, request, render_template_string
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def multiply():
    result = None
    error = ""
    if request.method == "POST":
        try:
            A = eval(request.form["matrixA"])
            B = eval(request.form["matrixB"])
            result = np.dot(A, B).tolist()
        except Exception as e:
            error = str(e)
    return render_template_string("""
        <html><head><title>Matrix Multiplication</title><style>
        body { font-family: Arial; margin: 40px; }
        textarea { width: 300px; height: 100px; }
        </style></head><body>
        <h2>Multiply Two Matrices</h2>
        <form method="POST">
            Matrix A: <br><textarea name="matrixA">[[1,2],[3,4]]</textarea><br>
            Matrix B: <br><textarea name="matrixB">[[5,6],[7,8]]</textarea><br>
            <button type="submit">Multiply</button>
        </form>
        {% if result %}<p>Result: {{ result }}</p>{% endif %}
        <p style="color:red;">{{ error }}</p>
        </body></html>
    """, result=result, error=error)
        