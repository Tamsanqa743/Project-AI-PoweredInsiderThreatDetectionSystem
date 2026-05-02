import pandas as pd
import joblib
import shap
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

# surpress warnings
warnings.filterwarnings("ignore")

# read in insider threat data
insider_threat_data = pd.read_csv('insider_threat_clean_dataset.csv')

# columns needing entries changed to numerical value equivalents
columns_to_encode = ['employee_department','employee_campus','employee_position', 'employee_origin_country']
 
# perform encoding for all target columns
for col in columns_to_encode:
    insider_threat_data[col] = insider_threat_data[col].astype('category').cat.codes



X = insider_threat_data[['employee_classification','total_printed_pages','num_printed_pages_off_hours','total_files_burned','burned_from_other','is_abroad','trip_day_number','hostility_country_level','num_entries','num_unique_campus','late_exit_flag','entry_during_weekend'
]]

# data_subset_x = insider_threat_data.sample(n=5000, random_state=42) # take subset of data for shap_value calculation

y = insider_threat_data[['is_malicious']]

#split data into training set and into testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize model
random_forest_model = RandomForestClassifier(random_state=42)

# create parameter grid
parameter_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 15, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid_searcher = GridSearchCV(
    estimator=random_forest_model,
    param_grid=parameter_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=2

)

print("Searching for grace...")

# run grid search
grid_searcher.fit(X_train, y_train)

# filename trained model will be saved as
filename = 'insider_threat_detector.joblib'

# filename for computed shap values
shap_values_filename = 'computed_shap_values.joblib'

# filename for expected_value from explainer
explainer_filename = 'explainer.joblib'

# y_pred = random_forest_model.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)

# print(f"Accuracy: {accuracy:.2f}")
# print("\nClassification Report:\n", classification_rep)



print("\nBest Parameters:")
print(grid_searcher.best_params_)

print("\nBest Cross-Validation Score:")
print(grid_searcher.best_score_)


final_random_forest_model = grid_searcher.best_estimator_

# dump trained model
joblib.dump(final_random_forest_model, filename)

# initialize explainer
prediction_explainer = shap.TreeExplainer(final_random_forest_model)

# save explainer expected value
joblib.dump(prediction_explainer, explainer_filename)


y_pred = final_random_forest_model.predict(X_test)

print("\nTest Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))