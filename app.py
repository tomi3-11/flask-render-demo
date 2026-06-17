from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    with open("version.txt") as file:
        version = file.read().strip()

    return render_template(
        "index.html",
        version=version,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
