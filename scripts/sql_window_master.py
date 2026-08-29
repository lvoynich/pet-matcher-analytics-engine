import sqlite3
import pandas as pd

conn = sqlite3.connect("pet_finder_warehouse.db")
cursor = conn.cursor()

# 1. Create an expanded shelter location table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shelter_locations (
    shelter_id TEXT,
    breed_name TEXT,
    state TEXT,
    available_dogs_count INTEGER
)
""")

# Insert mock operational geographic data
mock_locations = [
    ('S-01', 'Golden Retriever', 'WI', 12),
    ('S-02', 'French Bulldog', 'WI', 3),
    ('S-03', 'Border Collie', 'IL', 8),
    ('S-04', 'Golden Retriever', 'IL', 15),
    ('S-05', 'French Bulldog', 'IL', 14),
    ('S-06', 'Border Collie', 'WI', 2)
]

cursor.executemany("INSERT OR REPLACE INTO shelter_locations VALUES (?,?,?,?)", mock_locations)
conn.commit()

# 2. Analytics Engineering Window Function Model
# We rank the availability of each breed WITHIN each state
window_query = """
SELECT 
    state,
    UPPER(breed_name) as breed,
    available_dogs_count,
    RANK() OVER (
        PARTITION BY state 
        ORDER BY available_dogs_count DESC
    ) as regional_availability_rank
FROM 
    shelter_locations;
"""

final_report = pd.read_sql_query(window_query, conn)
print("\n🏅 Analytics Engineering Masterpiece: Regional ranks generated using Window Functions!")
print(final_report)

conn.close()
