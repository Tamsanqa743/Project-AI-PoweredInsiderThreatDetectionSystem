from flask import Flask, render_template, url_for
import os

template_dir = os.path.abspath('Presentation/templates/') # custom template directory path
static_dir = os.path.abspath('Presentation/static/') # custom static directory path
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)