from flask import Flask, render_template, url_for, request, flash
from werkzeug.utils import secure_filename
import os
from Controllers.file_controller import file_controller

template_dir = os.path.abspath('Presentation/templates/') # custom template directory path
static_dir = os.path.abspath('Presentation/static/') # custom static directory path
UPLOAD_FOLDER = os.path.abspath('Uploaded_files/') # folder uploaded files are stored
ALLOWED_EXTENSIONS = {'csv'} # file extensions allowed for upload
secret_key = 'DHEQJdxagshd2eg623829273273'


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # configure upload folder
app.config['SECRET_KEY'] = secret_key
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    '''handle file upload'''
    if request.method == 'POST':
        file = request.files['file']
        file_controller.file_upload(file, UPLOAD_FOLDER)
        flash("Success")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)