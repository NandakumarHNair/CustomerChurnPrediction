import pandas as pd
import sqlite3

def load_data_from_db(db_path):
    """Load customer data from SQLite database."""
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM customers;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def clean_data(df):
    """Clean and preprocess the customer data."""
    # Example cleaning steps:
    df = df.dropna()  # Drop missing values
    
    # Convert categorical variables to numeric
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['has_cr_card'] = df['has_cr_card'].astype(int)
    df['is_active_member'] = df['is_active_member'].astype(int)

    return df

def save_clean_data(df, file_path):
    """Save the cleaned data to CSV."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    db_path = 'customer_churn.db'  # Path to your SQLite database
    output_path = 'data/clean_customer_data.csv'
    
    # Step 1: Load the raw data from the SQLite database
    df = load_data_from_db(db_path)
    
    # Step 2: Clean the data
    df_clean = clean_data(df)
    
    # Step 3: Save the cleaned data to a new CSV file
    save_clean_data(df_clean, output_path)
    
    print(f"Data cleaning completed. Cleaned data saved to {output_path}.")
