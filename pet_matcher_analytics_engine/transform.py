import sqlite3
import pandas as pd

# 1. Connect to the database established in Phase 1
conn = sqlite3.connect("pet_finder_warehouse.db")

# 2. The Analytics Engineering Transformation Step
# We use SQL to calculate an 'adaptability_score' based on the breed traits
analytics_query = """
SELECT 
    UPPER(breed_name) AS breed_name_clean,
    size_category,
    energy_level,
    good_with_kids,
    -- Business Logic: Higher score means the dog adapts easier to typical families
    (good_with_kids * 2) - (energy_level) AS adaptability_score
FROM 
    raw_breed_data
ORDER BY 
    adaptability_score DESC;
"""

# Run the SQL model and view the structured data
transformed_df = pd.read_sql_query(analytics_query, conn)

# 3. Create the clean, production-ready table (The "Silver" layer)
transformed_df.to_sql("dim_cleaned_breeds", conn, if_exists="replace", index=False)

print("\n📊 Analytics Engineering Alert: Production tables successfully generated!")
print(transformed_df)

conn.close()
