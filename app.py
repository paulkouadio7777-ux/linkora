from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Linkora</title>
    </head>

    <body>
        <h1>Linkora 🚀</h1>
        <p>Bienvenue sur Linkora.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
