from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.utils.multiclass import unique_labels

class metrics_exporter:

    # @staticmethod
    # def export_confusion_matrix_latex(y_true, y_pred, filename="confusion_matrix.tex"):
    #     cm = confusion_matrix(y_true, y_pred)
    #     labels = sorted(set(y_true))

    #     latex = []
    #     latex.append("\\begin{table}[h]")
    #     latex.append("\\centering")
    #     latex.append("\\begin{tabular}{c|" + "c" * len(labels) + "}")
    #     latex.append("\\hline")

    #     # Header
    #     header = "Actual \\textbackslash Predicted & " + " & ".join(str(l) for l in labels) + " \\\\"
    #     latex.append(header)
    #     latex.append("\\hline")

    #     # Rows
    #     for i, row in enumerate(cm):
    #         row_str = str(labels[i]) + " & " + " & ".join(map(str, row)) + " \\\\"
    #         latex.append(row_str)

    #     latex.append("\\hline")
    #     latex.append("\\end{tabular}")
    #     latex.append("\\caption{Confusion Matrix for Random Forest Classifier}")
    #     latex.append("\\end{table}")

    #     with open(filename, "w") as f:
    #         f.write("\n".join(latex))

    @staticmethod
    def export_classification_metrics(y_true, y_pred, filename="model_evaluation.txt"):
        # Compute metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='binary')
        recall = recall_score(y_true, y_pred, average='binary')
        f1 = f1_score(y_true, y_pred, average='binary')
        cm = confusion_matrix(y_true, y_pred)

        # Write to file
        with open(filename, "w") as f:
            f.write("Random Forest Model Evaluation\n")
            f.write("===============================\n\n")

            f.write(f"Accuracy:  {accuracy:.4f}\n")
            f.write(f"Precision: {precision:.4f}\n")
            f.write(f"Recall:    {recall:.4f}\n")
            f.write(f"F1 Score:  {f1:.4f}\n\n")


    @staticmethod
    def export_confusion_matrix_latex(y_true, y_pred, filename="confusion_matrix.tex"):

        labels = unique_labels(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred, labels=labels)

        # Extract values (binary classification only)
        tn, fp, fn, tp = cm.ravel()

        latex = []
        latex.append("\\begin{table}[h]")
        latex.append("\\centering")
        latex.append("\\begin{tabular}{|c|c|c|}")
        latex.append("\\hline")

        # Header row
        latex.append(" & Predicted Negative & Predicted Positive \\\\")
        latex.append("\\hline")

        # Actual Negative row
        latex.append(
            f"Actual Negative & TN ({tn}) & FP ({fp}) \\\\"
        )
        latex.append("\\hline")

        # Actual Positive row
        latex.append(
            f"Actual Positive & FN ({fn}) & TP ({tp}) \\\\"
        )
        latex.append("\\hline")

        latex.append("\\end{tabular}")
        latex.append("\\caption{Confusion Matrix for Random Forest Classifier}")
        latex.append("\\end{table}")

        with open(filename, "w") as f:
            f.write("\n".join(latex))