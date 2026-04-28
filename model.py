import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib



# read in insider threat data
insider_threat_data = pd.read_csv('insider_threat_clean_dataset.csv')

# columns needing entries changed to numerical value equivalents
columns_to_encode = ['employee_department','employee_campus','employee_position', 'employee_origin_country']
 
# perform encoding for all target columns
for col in columns_to_encode:
    insider_threat_data[col] = insider_threat_data[col].astype('category').cat.codes



X = insider_threat_data[['employee_department','employee_campus','employee_position','employee_seniority_years','is_contractor','employee_classification','has_foreign_citizenship','has_criminal_record','has_medical_history','employee_origin_country','total_printed_pages','num_printed_pages_off_hours','total_files_burned','burned_from_other','is_abroad','trip_day_number','hostility_country_level','num_entries','num_unique_campus','late_exit_flag','entry_during_weekend'
]]
y = insider_threat_data[['is_malicious']]

#split data into training set and into testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=250, random_state=42)
rf_classifier.fit(X_train, y_train)

# filename trained model will be saved as
filename = 'insider_threat_detector.joblib'

# dump trained model
joblib.dump(rf_classifier, filename)

y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)

