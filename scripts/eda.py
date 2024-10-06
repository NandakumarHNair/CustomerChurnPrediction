import pandas as pd
import matplotlib.pyplot as plt
import os

def load_clean_data(file_path):
    """Load cleaned customer data."""
    return pd.read_csv(file_path)

def plot_churn_trends(df):
    """Plot churn trends based on various features."""
    # Example: Churn by Gender
    gender_churn = df.groupby('gender')['churn'].mean()
    gender_churn.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Churn Rate by Gender')
    plt.xlabel('Gender (1=Male, 0=Female)')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=0)
    plt.savefig('visualizations/churn_trends.png')
    plt.close()

def main():
    data_path = 'data/clean_customer_data.csv'
    df = load_clean_data(data_path)
    plot_churn_trends(df)
    print("EDA completed and visualizations saved.")

if __name__ == "__main__":
    main()
