import pandas as pd
import numpy  as np
import joblib



class Core:
    def __init__(self):

        # exported file names from training
        self.model_filename = 'insider_threat_detector.joblib'
        # shap_values_filename = 'computed_shap_values.joblib'
        self.explainer_filename = 'explainer.joblib'

        # read in insider threat data
        # insider_threat_data = pd.read_csv('insider_threat_clean_dataset.csv')
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

        self.behaviour_dict = {1:'Malicious', 0: 'Normal'} # behaviour malicious or normal based on prediction


    def explain_prediction(self,model, shap_explainer, input_data_frame_x, max_top_features=5, class_index=1):

            feature_contributions_array = shap_explainer.shap_values(input_data_frame_x)[0] # feature contributions
            to_sort_values = feature_contributions_array # copy feature_contributions_array 

            # average model output for random forest classifier
            base = shap_explainer.expected_value[class_index]

            # make prediction
            prediction = model.predict_proba(input_data_frame_x)
            # print("prediction:", prediction)
            prediction_text = f"{prediction[0][class_index]: .2f}"
            # print("Prediction text:", prediction_text)


            # explanation string
            description = [f"Prediction: {prediction_text} (baseline: {base: .2f})\n"]

            # rank features by absolute SHAP values to max of max_top_features
            top_feature_indices = np.argsort(-np.abs(to_sort_values[:,class_index]))[:max_top_features]

            # print("top feature indeces:", top_feature_indices)
            sorted_feature_contributions = [(to_sort_values[i, 0], to_sort_values[i, class_index]) for i in top_feature_indices]
            
            # for val in sorted_feature_contributions:
            #     print("Value:", val[class_index])
            for feature in top_feature_indices:
                contribution = feature_contributions_array[feature][class_index]
                # determine whether feature increases or decreases prediction
                # if contribution > 0:
                #     prediction_direction = "increased"
                # else:
                #     prediction_direction = "decreased"

                description.append(f"{self.user_friendly_category_names[input_data_frame_x.columns[feature]]} pushed behaviour prediction towards being {self.behaviour_dict[class_index]}\n")

            return description
        

    def predict_behaviour(self, model, input_data_frame):
        '''predict behaviour and return result'''
        return model.predict(input_data_frame)[0] # return prediction as number


    def read_and_process_input_data(self,input_filename):
        '''read csv and drop columns not used for prediction'''
        data_frame = pd.read_csv(input_filename)
        data_frame = data_frame.drop(columns=self.columns_to_drop)
        return data_frame
    # returns array of prediction and description

    def analyse(self,ext_filename):
        df = self.read_and_process_input_data(self.upload_folder+ext_filename)
        prediction = self.predict_behaviour(self.trained_model, df)
        return self.behaviour_dict[prediction], self.explain_prediction(self.trained_model, self.explainer, df, 5, prediction)




# new_data = {
#     'total_printed_pages': 85,
#     'num_printed_pages_off_hours': 40,
#     'total_files_burned': 15,
#     'burned_from_other': 1,
#     'is_abroad': 0,
#     'trip_day_number': 0.0,
#     'num_entries': 12,
#     'num_unique_campus': 2,
#     'late_exit_flag': 1,
#     'entry_during_weekend': 1
# }

# new_data_2 = {
#     'total_printed_pages': 12,
#     'num_printed_pages_off_hours': 0,
#     'total_files_burned': 1,
#     'burned_from_other': 0,
#     'is_abroad': 0,
#     'trip_day_number': 0.0,
#     'num_entries': 4,
#     'num_unique_campus': 1,
#     'late_exit_flag': 0,
#     'entry_during_weekend': 0
# }



# new_df = pd.DataFrame([new_data])
# new_df_2 = pd.DataFrame([new_data_2])


# y_pred = trained_model.predict(new_df)[0] # extract prediction value into int


# print('first prediction', y_pred)
# y_pred_2 = trained_model.predict(new_df_2)
# print('second prediction:', y_pred_2)





# print("Expected Malicious prediction:", explain_prediction(self.trained_model, explainer, new_df_2,5, y_pred_2[0]))
