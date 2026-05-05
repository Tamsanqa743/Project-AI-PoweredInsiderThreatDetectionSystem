import pandas as pd
import numpy  as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import shap
import matplotlib

# exported file names from training
model_filename = 'insider_threat_detector.joblib'
# shap_values_filename = 'computed_shap_values.joblib'
explainer_filename = 'explainer.joblib'

# read in insider threat data
insider_threat_data = pd.read_csv('insider_threat_clean_dataset.csv')

# load trained model from file
trained_model = joblib.load(model_filename)

# load explainer value
explainer = joblib.load(explainer_filename)



new_data = {
    'employee_classification': 2,
    'total_printed_pages': 85,
    'num_printed_pages_off_hours': 40,
    'total_files_burned': 15,
    'burned_from_other': 1,
    'is_abroad': 0,
    'trip_day_number': 0.0,
    'hostility_country_level': 0,
    'num_entries': 12,
    'num_unique_campus': 2,
    'late_exit_flag': 1,
    'entry_during_weekend': 1
}

new_data_2 = {
    'employee_classification': 2,
    'total_printed_pages': 12,
    'num_printed_pages_off_hours': 0,
    'total_files_burned': 1,
    'burned_from_other': 0,
    'is_abroad': 0,
    'trip_day_number': 0.0,
    'hostility_country_level': 0,
    'num_entries': 4,
    'num_unique_campus': 1,
    'late_exit_flag': 0,
    'entry_during_weekend': 0
}



new_df = pd.DataFrame([new_data])
new_df_2 = pd.DataFrame([new_data_2])


y_pred = trained_model.predict(new_df)[0] # extract prediction value into int


print('first prediction', y_pred)
# y_pred = trained_model.predict(new_df_2)
# print('second prediction:', y_pred)

print('feature length', len(['employee_classification','total_printed_pages','num_printed_pages_off_hours','total_files_burned','burned_from_other','is_abroad','trip_day_number','hostility_country_level','num_entries','num_unique_campus','late_exit_flag','entry_during_weekend'
]))

def predict_and_explain(model, shap_explainer, input_data_frame_x, max_top_features=5, class_index=1):

    feature_contributions_array = shap_explainer.shap_values(input_data_frame_x)[0] # feature contributions
    to_sort_values = feature_contributions_array # copy feature_contributions_array 

    # average model output for random forest classifier
    base = shap_explainer.expected_value[class_index]

    # make prediction
    prediction = model.predict_proba(input_data_frame_x)
    print("prediction:", prediction)
    prediction_text = f"{prediction[0][class_index]: .2f}"


    # explanation string
    description = f"Prediction: {prediction_text} (baseline: {base: .2f})\n"
    description += "Key factors:\n"

    # rank features by absolute SHAP values to max of max_top_features
    top_feature_indices = np.argsort(-np.abs(to_sort_values[:,class_index]))[:max_top_features]
    print("feature contribution array:", feature_contributions_array)

    print("top feature indeces:", top_feature_indices)
    sorted_feature_contributions = [(to_sort_values[i, 0], to_sort_values[i, class_index]) for i in top_feature_indices]
    
    for val in sorted_feature_contributions:
        print("Value:", val[class_index])

# look into using baseline to influence the explanation in terms of strength of contribution to a predicition

    for feature in top_feature_indices:
        contribution = feature_contributions_array[feature][class_index]

        # determine whether feature increases or decreases prediction
        if contribution > 0:
            direction = "increased"
        else:
            direction = "decreased"
        
        # determine qualitative strength
        if abs(contribution) > 0.1:
            strength = "strongly"
        else:
            strength = "slightly"

        description += (f" - {input_data_frame_x.columns[feature]} "
                        f"{strength} {direction} the prediction\n"
        ) 


        # shap.plots.waterfall(shap_explainer(input_data_frame_x)[0][0])
    # return description
    return description  
    

print("Expected Malicious prediction:", predict_and_explain(trained_model, explainer, new_df,5, y_pred))
