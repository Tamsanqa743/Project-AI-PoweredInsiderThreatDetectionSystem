import pandas as pd
import numpy  as np
import joblib, os
from pathlib import Path



class core:
    def __init__(self):

        # exported file names from training
        self.parent_path = Path(__file__).parent/'..'
        self.model_filename = self.parent_path/'models/insider_threat_detector.joblib'
        print(os.path.curdir)
        self.explainer_filename = self.parent_path/'models/explainer.joblib'
        self.upload_folder = './Uploaded_files/'

        # load trained model from file
        self.trained_model = joblib.load(self.model_filename)

        # load explainer value
        self.explainer = joblib.load(self.explainer_filename)

        self.columns_to_drop = ['employee_department', 'employee_campus', 'employee_position', 'employee_seniority_years', 'is_contractor', 'has_foreign_citizenship', 'has_criminal_record', 'has_medical_history', 'employee_origin_country','is_malicious', 'employee_classification', 'hostility_country_level']

        self.user_friendly_category_names = {
            'total_printed_pages': 'Total number of printed pages',
            'num_printed_pages_off_hours': 'Number of printed pages off hours',
            'total_files_burned': 'Total files burned',
            'burned_from_other': 'Files burned from other',
            'is_abroad': 'Is abroad',
            'trip_day_number': 'Number of trip days',
            'num_entries': 'Number of entries',
            'num_unique_campus': 'Number of unique campus visits',
            'late_exit_flag': 'Late exits flag',
            'entry_during_weekend': 'Entry during the weekend'}

        self.behaviour_dict = {1:'Malicious', 0: 'Normal'} # behaviour malicious or normal based on classification


    def explain_classification(self,model, shap_explainer, input_data_frame_x, max_top_features=5, class_index=1):

            feature_contributions_array = shap_explainer.shap_values(input_data_frame_x)[0] # feature contributions
            to_sort_values = feature_contributions_array # copy feature_contributions_array 

            # make classification
            classification = model.predict_proba(input_data_frame_x)
            classification_confidence = f"{classification[0][class_index]*100: .2f}%"

            # explanation string
            description = []

            # rank features by absolute SHAP values to max of max_top_features
            top_feature_indices = np.argsort(-np.abs(to_sort_values[:,class_index]))[:max_top_features]
            
            for feature in top_feature_indices:
                description.append(f"{self.user_friendly_category_names[input_data_frame_x.columns[feature]]}\n")

            return description, classification_confidence
        

    def classify_behaviour(self, model, input_data_frame):
        '''predict behaviour and return result'''
        return model.predict(input_data_frame)[0] # return classification as number


    def read_and_process_input_data(self,input_filename):
        '''read csv and drop columns not used for classification'''
        data_frame = pd.read_csv(input_filename)
        data_frame = data_frame.drop(columns=self.columns_to_drop)
        return data_frame # returns array of classification and description

    def analyse(self,ext_filename):
        '''analyse behaviour data and return classifiaction with explanation'''
        df = self.read_and_process_input_data(self.upload_folder+ext_filename)
        classification = self.classify_behaviour(self.trained_model, df)
        return self.behaviour_dict[classification], self.explain_classification(self.trained_model, self.explainer, df, 5, classification)