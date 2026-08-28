# Insider Threat Detection System

A machine learning-based web application for detecting potentially malicious insider activity using user behavioural data.

The system uses a **Random Forest classifier** to classify user behaviour as either **normal** or **malicious insider activity**. It provides an end-to-end workflow covering data preprocessing, model training, evaluation, deployment, and model interpretability using **SHAP (SHapley Additive exPlanations)**.

The project is implemented in **Python** and is designed for deployment on **Windows** using a Python virtual environment.

---

## 1. System Overview

The Insider Threat Detection System analyses uploaded `.csv` behavioural data and uses a trained Random Forest machine learning model to determine whether observed user behaviour is normal or indicative of malicious insider activity.

The system consists of the following components:

- **Data preprocessing** – Cleans and prepares behavioural data for machine learning.
- **Model training** – Trains a Random Forest classification model.
- **Parameter tuning** – Optimises model parameters to improve classification performance.
- **Model evaluation** – Calculates accuracy, precision, recall, and F1-score.
- **Model deployment** – Deploys the trained model through a Flask web application.
- **Model interpretability** – Uses SHAP to explain model predictions.
- **CSV-based inference** – Allows users to upload behavioural `.csv` files for classification.

### High-Level Workflow

```text
Behavioural CSV Data
        |
        v
Data Preprocessing
        |
        v
Random Forest Model
        |
        +--------------> Prediction
        |
        v
SHAP Explainer
        |
        v
Prediction + Explanation
        |
        v
Flask Web Application
```
