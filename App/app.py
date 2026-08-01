import os
from flask import Flask, render_template, request, flash, redirect, jsonify
from werkzeug.utils import secure_filename
from Controllers.file_controller import file_controller
from Controllers.core_controller import core_controller

template_dir = os.path.abspath('Presentation/templates/') # custom template directory path
static_dir = os.path.abspath('Presentation/static/') # custom static directory path
UPLOAD_FOLDER = os.path.abspath('Uploaded_files/') # folder uploaded files are stored
ALLOWED_EXTENSIONS = {'csv'} # file extensions allowed for upload
secret_key = 'DHEQJdxagshd2eg623829273273'
display_results = False

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
    return render_template('analysis.html', saved_filename=filename, display_results = display_results)


@app.route('/analyse', methods=['POST'])
def analyse():
    '''start data analysis'''
    result = core_con.analyse_behaviour(file_con.get_filename())
    description = result[1][0] # classification explanation
    classification_confidence = result[1][1] # classification confidence
    
    classification = result[0] # classification result
    flash("Analysis Complete!", "success")
    display_results = True # set flag to show results on page
    return render_template('analysis.html', classification_description=description, classification_output=classification,classification_confidence=classification_confidence, saved_filename=file_con.get_filename(), display_results = display_results)

@app.route('/upload_new_file',methods=['POST'])
def upload_new_file():
    '''Redirect to upload page'''
    return redirect('/')

@app.route('/analyse2', methods=['POST', 'GET'])
def analyse2():
    '''start data analysis'''
    result = core_con.analyse_behaviour(file_con.get_filename())
    description = result[1][0] # classification explanation
    classification_confidence = result[1][1] # classification confidence
    
    classification = result[0] # classification result
    flash("Analysis Complete!", "success")

    feature_styling = "green" if classification == "Normal" else "Orange"
    classification_styling = "green" if classification == "Normal" else "red" 
    contributing_features_list = ""

    for feature in description:
        contributing_features_list += f'<li style="color:{feature_styling}">{feature}</li>'

    formatted_results_content = f'''
        <div class="results-container">
        <h3 class="mt-3 ms-3"><b>Threat Report</b></h3>
            <div class="mt-3 ms-3 prediction-breakdown"><p><b>User Behaviour: </b><span style="color: {classification_styling}"><b>{classification}</b>
                </span></p><p><b>Classification Confidence:</b><b>{classification_confidence}</b></p>
                <p><b>Key risk indicators that influenced the classification:<br></p>
                {contributing_features_list}
            </div>
        </div>
        '''
    return jsonify({"html_content":formatted_results_content})

if __name__ == "__main__":
    app.run(debug=True)