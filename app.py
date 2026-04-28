import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib



model_filename = './models/insider_threat_detector.joblib'
loaded_model = joblib.load(model_filename)

new_data = {
    'employee_department': 0,
    'employee_campus': 0,
    'employee_position': 0,
    'employee_seniority_years': 7,
    'is_contractor': 0,
    'employee_classification': 2,
    'has_foreign_citizenship': 0,
    'has_criminal_record': 0,
    'has_medical_history': 0,
    'employee_origin_country': 0,
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
    'employee_department': 0,
    'employee_campus': 0,
    'employee_position': 0,
    'employee_seniority_years': 5,
    'is_contractor': 0,
    'employee_classification': 2,
    'has_foreign_citizenship': 0,
    'has_criminal_record': 0,
    'has_medical_history': 0,
    'employee_origin_country': 0,
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

y_pred = loaded_model.predict(new_df)


print('first prediction', y_pred)
y_pred = loaded_model.predict(new_df_2)
print('second prediction:', y_pred)
