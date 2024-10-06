import sqlite3
import pandas as pd

# Path to your SQLite database
db_path = 'customer_churn.db'

# Path to your CSV file
csv_file_path = 'data/customer_data.csv'

# Step 1: Load the CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Step 2: Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 3: Insert data row by row with INSERT OR REPLACE to handle duplicates
for index, row in df.iterrows():
    cursor.execute("""
        INSERT OR REPLACE INTO customers (customer_id, gender, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary, churn)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['customer_id'],
        row['gender'],
        row['age'],
        row['tenure'],
        row['balance'],
        row['num_of_products'],
        row['has_cr_card'],
        row['is_active_member'],
        row['estimated_salary'],
        row['churn']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data loaded successfully into the 'customers' table.")
