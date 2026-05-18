from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os
from Controllers.file_controller import file_controller
from Controllers.core_controller import core_controller

template_dir = os.path.abspath('Presentation/templates/') # custom template directory path
static_dir = os.path.abspath('Presentation/static/') # custom static directory path
UPLOAD_FOLDER = os.path.abspath('Uploaded_files/') # folder uploaded files are stored
ALLOWED_EXTENSIONS = {'csv'} # file extensions allowed for upload
secret_key = 'DHEQJdxagshd2eg623829273273'

file_con = file_controller()
core_con = core_controller()

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
        if request.files['file'].filename == '': 
            flash('No File Selected! Try Again', 'danger')
            return render_template('index.html')

        file = request.files['file']
        file_con.file_upload(file, UPLOAD_FOLDER)
        filename = secure_filename(file.filename)
        flash("File Upload Successful", "success")
    return render_template('analysis.html', saved_filename=filename)


@app.route('/analyse', methods=['POST'])
def analyse():
    '''start data analysis'''
    result = core_con.analyse_behaviour(file_con.get_filename())
    description = result[1][0] # classification explanation
    classification_confidence = result[1][1] # classification confidence
    
    classification = result[0] # classification result
    flash("Analysis Complete!", "success")
    return render_template('analysis.html', classification_description=description, classification_output=classification,classification_confidence=classification_confidence, saved_filename=file_con.get_filename())

@app.route('/upload_new_file',methods=['POST'])
def upload_new_file():
    '''Redirect to upload page'''
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)