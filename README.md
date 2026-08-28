Insider Threat Detection System

A machine learning-based web application for detecting potentially malicious insider activity using user behavioural data. The system uses a Random Forest classifier to classify behavioural activity as either normal or malicious insider activity.

The application provides an end-to-end workflow covering data preprocessing, model training, evaluation, deployment, and model interpretability using SHAP (SHapley Additive exPlanations).

The project is implemented in Python and is designed for reproducible deployment on Windows using a Python virtual environment.

1. System Overview

The Insider Threat Detection System analyses uploaded .csv behavioural data and uses a trained Random Forest machine learning model to determine whether observed user behaviour is normal or indicative of malicious insider activity.

The system consists of the following major components:

Data preprocessing – Cleans and prepares behavioural data for machine learning.
Model training – Trains a Random Forest classification model.
Parameter tuning – Optimises model parameters to improve classification performance.
Model evaluation – Calculates performance metrics including accuracy, precision, recall, and F1-score.
Model deployment – Deploys the trained model through a Flask web application.
Model interpretability – Uses SHAP to provide explanations for model predictions.
CSV-based inference – Allows users to upload behavioural .csv data through the web interface for classification.
High-Level Workflow
Behavioural CSV Data
        │
        ▼
 Data Preprocessing
        │
        ▼
 Random Forest Model
        │
        ├──────────────► Prediction
        │
        ▼
   SHAP Explainer
        │
        ▼
 Prediction + Explanation
        │
        ▼
 Flask Web Application

2. Software Requirements

The application is developed in Python and is intended to run on a Windows operating system.

Prerequisites

The following software is required:

Python 3
virtualenv
pip
Windows operating system
Core Dependencies

The project uses the following primary Python libraries:

Dependency	Purpose
scikit-learn	Training and evaluation of the Random Forest classifier
pandas	Data manipulation and preprocessing
shap	Model interpretability and prediction explanations
Flask	Web application and model deployment

Additional dependencies required by the project are specified in requirements.txt.

3. Installation

Follow the steps below to set up the project on Windows.

3.1 Open the Application Directory

Open a terminal and navigate to the project's App directory.

For example:

cd path\to\App

3.2 Create a Virtual Environment

Create a Python virtual environment using virtualenv:

python3 -m virtualenv venv


Note: Ensure that Python 3 and virtualenv are installed and available from the command line before running this command.

3.3 Activate the Virtual Environment

Activate the virtual environment:

venv\Scripts\activate


After successful activation, the terminal should indicate that the venv environment is active.

3.4 Install Dependencies

Install all required packages from requirements.txt:

pip install -r requirements.txt

3.5 Verify the Installation

To verify that the required dependencies have been installed:

pip list


Confirm that the required project dependencies are present in the package list.

4. Project Structure

A typical project structure is shown below:

App/
│
├── app.py
├── core.py
├── core_controller.py
├── model.py
├── metrics_exporter.py
├── requirements.txt
│
├── models/
│   ├── insider_threat_detector.pkl
│   └── explainer.pkl
│
└── venv/


The exact structure may vary depending on the files included in the project.

5. Model Training

The machine learning model can be trained by executing model.py.

Ensure that the virtual environment is activated before running the training process.

python3 model.py


The training process performs the required data processing and model training. Once training has successfully completed, the trained model and SHAP explainer are exported to the models directory.

The generated files are:

models/
├── insider_threat_detector.pkl
└── explainer.pkl

Generated Artifacts
File	Description
insider_threat_detector.pkl	Serialized trained Random Forest classifier
explainer.pkl	Serialized SHAP explainer used to interpret model predictions

These artifacts are subsequently loaded by the Flask application during inference.

6. Model Evaluation

Model evaluation is handled by metrics_exporter.py.

The evaluation component calculates performance metrics that can be used to assess the effectiveness of the trained classifier.

The metrics include:

Accuracy
Precision
Recall
F1-score

These metrics can be exported for further analysis and reporting.

7. Running the Application

After the model has been trained and the required model files have been generated, start the Flask application using:

python3 app.py


The Flask application will start a local web server.

By default, the application is accessible at:

http://127.0.0.1:5000/


Open the address in a web browser to access the application.

8. Application Usage

The application provides a web-based interface through which users can interact with the trained machine learning model.

The general workflow is:

Start the Flask application.
Open the application in a web browser.
Upload the required behavioural .csv file.
The application preprocesses the uploaded data.
The trained Random Forest model performs classification.
The system returns the prediction results.
SHAP is used to provide interpretability for the model's predictions.
9. Source Code Documentation
app.py

The entry point of the Flask web application.

Responsibilities include:

Starting the Flask application.
Defining application routes.
Handling HTTP requests.
Receiving uploaded behavioural data.
Communicating with the controller and core application logic.
Returning results to the frontend.
core.py

Contains the core business and machine learning inference logic.

Responsibilities include:

Data preprocessing.
Preparing behavioural data for inference.
Interacting with the trained machine learning model.
Processing model predictions.
Supporting SHAP-based model explanations.
core_controller.py

Acts as an intermediary between the Flask application and the core business logic.

Responsibilities include:

Managing the request flow.
Coordinating calls between the presentation layer and core logic.
Ensuring that requests are processed appropriately.
model.py

Responsible for machine learning model development and training.

Responsibilities include:

Loading and preparing training data.
Data preprocessing.
Training the Random Forest classifier.
Model parameter tuning.
Evaluating model performance.
Creating the SHAP explainer.
Exporting the trained model and explainer to the models directory.
metrics_exporter.py

Responsible for calculating and exporting model evaluation metrics.

The component supports metrics such as:

Accuracy
Precision
Recall
F1-score

These results can be used for model analysis and reporting.

10. System Architecture

The application follows a layered architecture designed to separate the web interface, application control flow, business logic, machine learning model, and evaluation functionality.

┌─────────────────────────────────────┐
│       Presentation Layer            │
│              app.py                 │
│         Flask Web Application       │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Controller Layer            │
│        core_controller.py            │
│       Request Flow Management        │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│         Business Logic Layer         │
│              core.py                 │
│      Preprocessing & Inference       │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│            Model Layer               │
│             model.py                 │
│        Random Forest + SHAP          │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Evaluation Layer            │
│        metrics_exporter.py           │
│ Accuracy / Precision / Recall / F1  │
└─────────────────────────────────────┘

Architectural Layers
Layer	Component	Responsibility
Presentation	app.py	Flask interface and HTTP requests
Controller	core_controller.py	Request coordination and flow management
Business Logic	core.py	Data preprocessing and inference logic
Model	model.py	Model training, tuning, and SHAP integration
Evaluation	metrics_exporter.py	Model performance evaluation and metric export
11. Trained Model Files

The trained machine learning model and associated artifacts are stored as serialized .pkl files.

insider_threat_detector.pkl

Contains the trained Random Forest classifier used to classify behavioural data.

explainer.pkl

Contains the SHAP explainer used to provide interpretability for the model's predictions.

Both files are generated automatically when the training process is executed:

python3 model.py


The files are saved in:

models/


During application execution, app.py and the underlying application logic load these artifacts to perform inference on uploaded behavioural data.

12. Typical Execution Workflow

For a fresh installation, the recommended execution sequence is:

Step 1 — Create the environment
python3 -m virtualenv venv

Step 2 — Activate the environment
venv\Scripts\activate

Step 3 — Install dependencies
pip install -r requirements.txt

Step 4 — Train the model
python3 model.py


This generates:

models/insider_threat_detector.pkl
models/explainer.pkl

Step 5 — Start the Flask application
python3 app.py

Step 6 — Open the application

Navigate to:

http://127.0.0.1:5000/


The system is then ready to process uploaded behavioural CSV files.

13. Troubleshooting
Virtual environment cannot be activated

Ensure that you are running the command from the project directory containing the venv folder:

venv\Scripts\activate

Dependencies are missing

Make sure the virtual environment is activated and reinstall the dependencies:

pip install -r requirements.txt

Model files are missing

Run the model training script before starting the application:

python3 model.py


Verify that the following files exist:

models/insider_threat_detector.pkl
models/explainer.pkl

Application cannot be accessed

Ensure that the Flask application is running:

python3 app.py


Then access:

http://127.0.0.1:5000/

14. Summary

The Insider Threat Detection System provides a complete machine learning pipeline for identifying potentially malicious insider behaviour from behavioural data.

The system combines:

Random Forest for classification.
Pandas for data preprocessing.
Scikit-learn for machine learning and evaluation.
SHAP for model interpretability.
Flask for web-based deployment.
Python virtual environments for reproducible dependency management.
