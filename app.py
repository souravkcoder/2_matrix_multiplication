from flask import Flask, request, render_template_string
import numpy as np
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def multiply():
    result = None
    error = ""
    matrixA = "[[1, 2], [3, 4]]"
    matrixB = "[[5, 6], [7, 8]]"

    if request.method == "POST":
        matrixA = request.form["matrixA"]
        matrixB = request.form["matrixB"]
        try:
            A = eval(matrixA)
            B = eval(matrixB)
            result = np.dot(A, B).tolist()
        except Exception as e:
            error = f"❌ Error: {str(e)}"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Matrix Multiplication</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f7f9fc;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                width: 90%;
                max-width: 600px;
                text-align: center;
            }
            textarea {
                width: 90%;
                height: 100px;
                margin: 10px 0;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                resize: none;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result, .error {
                margin-top: 20px;
                font-size: 16px;
            }
            .error {
                color: red;
            }
            .result pre {
                text-align: left;
                background: #f1f1f1;
                padding: 10px;
                border-radius: 5px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Matrix Multiplication</h2>
            <p>Enter matrices in Python list format (e.g., <code>[[1, 2], [3, 4]]</code>).</p>
            <form method="POST">
                <label>Matrix A:</label><br>
                <textarea name="matrixA">{{ matrixA }}</textarea><br>
                <label>Matrix B:</label><br>
                <textarea name="matrixB">{{ matrixB }}</textarea><br>
                <button type="submit">Multiply</button>
            </form>

            {% if result %}
            <div class="result">
                <strong>✅ Result:</strong>
                <pre>{{ result }}</pre>
            </div>
            {% endif %}

            {% if error %}
            <div class="error">{{ error }}</div>
            {% endif %}
        </div>
    </body>
    </html>
    """, result=result, error=error, matrixA=matrixA, matrixB=matrixB)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)
