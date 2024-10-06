import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

def load_clean_data(file_path):
    """Load cleaned customer data."""
    return pd.read_csv(file_path)

def build_logistic_regression(df):
    """Build and evaluate a logistic regression model."""
    X = df.drop('churn', axis=1)
    y = df['churn']

    # Add constant for intercept
    X = sm.add_constant(X)
    
    print(f"Data shape: {df.shape}")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Build the model
    model = sm.Logit(y_train, X_train).fit()
    print(model.summary())

    # Predictions
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob >= 0.5).astype(int)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_prob)
    cm = confusion_matrix(y_test, y_pred)

    print(f'Accuracy: {accuracy:.4f}')
    print(f'AUC: {auc:.4f}')
    print('Confusion Matrix:')
    print(cm)

    # Plot ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    plt.figure()
    plt.plot(fpr, tpr, label=f'ROC curve (area = {auc:.2f})')
    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    plt.savefig('visualizations/model_performance.png')
    plt.close()

def main():
    data_path = 'data/clean_customer_data.csv'
    df = load_clean_data(data_path)
    build_logistic_regression(df)
    print("Model building and evaluation completed.")

if __name__ == "__main__":
    main()
