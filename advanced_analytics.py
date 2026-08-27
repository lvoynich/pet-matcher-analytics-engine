import sqlite3
import pandas as pd

conn = sqlite3.connect("pet_finder_warehouse.db")
cursor = conn.cursor()

# 1. Simulate an operational transaction table (Like an Oracle EBS table)
cursor.execute("""
CREATE TABLE IF NOT EXISTS shelter_transactions (
    transaction_id INTEGER PRIMARY KEY,
    breed_name TEXT,
    days_in_shelter INTEGER,
    adoption_status TEXT
)
""")

# Insert mock transactional history data
mock_transactions = [
    (101, 'Golden Retriever', 14, 'Adopted'),
    (102, 'French Bulldog', 5, 'Adopted'),
    (103, 'Border Collie', 45, 'Adopted'),
    (104, 'Chihuahua', 60, 'Bosted'),
    (105, 'Greyhound', 30, 'Adopted'),
    (106, 'Golden Retriever', 21, 'Adopted'),
    (107, 'Border Collie', 35, 'Adopted'),
    (108, 'French Bulldog', 7, 'Adopted')
]

cursor.executemany("INSERT OR REPLACE INTO shelter_transactions VALUES (?,?,?,?)", mock_transactions)
conn.commit()

# 2. Advanced SQL Join & Aggregation Model
# We aggregate transactional logs against our core breed dimension table
advanced_query = """
SELECT 
    b.breed_name_clean,
    b.size_category,
    COUNT(t.transaction_id) as total_processed,
    AVG(t.days_in_shelter) as avg_days_to_adopt
FROM 
    dim_cleaned_breeds b
JOIN 
    shelter_transactions t ON UPPER(b.breed_name_clean) = UPPER(t.breed_name)
GROUP BY 
    1, 2
ORDER BY 
    avg_days_to_adopt ASC;
"""

analytics_results = pd.read_sql_query(advanced_query, conn)
print("\n📊 Enterprise Analytics Alert: Transaction metrics joined successfully!")
print(analytics_results)

conn.close()

