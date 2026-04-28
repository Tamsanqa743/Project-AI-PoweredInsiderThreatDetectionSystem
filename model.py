import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import warnings
warnings.filterwarnings('ignore')


# read in insider threat data
insider_threat_data = pd.read_csv('insider_threat_clean_dataset.csv')

columns_to_encode = ['employee_department','employee_campus','employee_position', 'employee_origin_country']
 

for col in columns_to_encode:
    insider_threat_data[col] = insider_threat_data[col].astype('category').cat.codes



X = insider_threat_data[['employee_department','employee_campus','employee_position','employee_seniority_years','is_contractor','employee_classification','has_foreign_citizenship','has_criminal_record','has_medical_history','employee_origin_country','total_printed_pages','num_printed_pages_off_hours','total_files_burned','burned_from_other','is_abroad','trip_day_number','hostility_country_level','num_entries','num_unique_campus','late_exit_flag','entry_during_weekend'
]]
y = insider_threat_data[['is_malicious']]

#split data into training set and into testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)

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

y_pred = rf_classifier.predict(new_df)


print(y_pred)
y_pred = rf_classifier.predict(new_df_2)
print('second prediction:', y_pred)

