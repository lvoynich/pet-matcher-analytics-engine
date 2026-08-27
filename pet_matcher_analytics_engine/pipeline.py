import sqlite3
import pandas as pd

# 1. Simulate the Data Engineering "Ingestion" step
# In a production environment, this would pull directly from a live web API.
raw_dog_data = {
    "breed_name": ["Golden Retriever", "French Bulldog", "Border Collie", "Chihuahua", "Greyhound"],
    "energy_level": [3, 2, 5, 2, 4],        # Scale of 1-5
    "exercise_needs": [4, 2, 5, 1, 3],     # Scale of 1-5
    "size_category": ["Large", "Small", "Medium", "Small", "Large"],
    "good_with_kids": [5, 5, 3, 2, 4],      # Scale of 1-5
    "grooming_needs": [3, 1, 3, 1, 1]       # Scale of 1-5
}

# Turn the raw data stream into a structured DataFrame
df = pd.DataFrame(raw_dog_data)

# 2. Establish a connection to our local database storage
conn = sqlite3.connect("pet_finder_warehouse.db")
cursor = conn.cursor()

# 3. Create the raw data landing table (The "Bronze" layer)
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_breed_data (
    breed_name TEXT,
    energy_level INTEGER,
    exercise_needs INTEGER,
    size_category TEXT,
    good_with_kids INTEGER,
    grooming_needs INTEGER
)
""")

# 4. Load the raw data into our database warehouse
df.to_sql("raw_breed_data", conn, if_exists="replace", index=False)
conn.commit()

print("🚀 Data Engineering Alert: Raw breed data successfully ingested into the warehouse!")
conn.close()
