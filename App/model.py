import pandas as pd
import joblib
import shap
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from metrics_exporter import metrics_exporter
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



X = insider_threat_data[['total_printed_pages','num_printed_pages_off_hours','total_files_burned','burned_from_other','is_abroad','trip_day_number','num_entries','num_unique_campus','late_exit_flag','entry_during_weekend']]

y = insider_threat_data[['is_malicious']]

#split data into training set and into testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize model
random_forest_model = RandomForestClassifier(random_state=42)

# create parameter grid
parameter_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2],
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

print("Performing Grid Search...")

# run grid search
grid_searcher.fit(X_train, y_train)

# filename trained model will be saved as
filename = './models/insider_threat_detector.joblib'

# filename for expected_value from explainer
explainer_filename = 'explainer.joblib'


print("\nBest Parameters:")
print(grid_searcher.best_params_)

print("\nBest Cross-Validation Score:")
print(grid_searcher.best_score_)


final_random_forest_model = grid_searcher.best_estimator_

# dump trained model
joblib.dump(final_random_forest_model, filename)

# initialize explainer
prediction_explainer = shap.TreeExplainer(final_random_forest_model)

# make predictions using test data
y_pred = final_random_forest_model.predict(X_test) 

metrics_exporter.export_classification_metrics(y_test, y_pred) # export metrics for test data
metrics_exporter.export_confusion_matrix_latex(y_test, y_pred, "confusion_matrix.tex") # export confusion matrix