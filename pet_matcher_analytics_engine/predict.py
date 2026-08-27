import sqlite3
import pandas as pd

# 1. Connect to the clean analytical data warehouse table
conn = sqlite3.connect("pet_finder_warehouse.db")

# Read the clean dimensions created by the Analytics Engineer
df = pd.read_sql_query("SELECT * FROM dim_cleaned_breeds", conn)

# 2. Simulate a Data Science User Profile (Input Data)
# Change these values to simulate a different type of owner!
user_profile = {
    "preferred_energy": 2,     # 1 = Couch Potato, 5 = Marathon Runner
    "preferred_kid_friendly": 5 # 1 = Independent, 5 = Super Family Friendly
}

# 3. The Machine Learning / Statistical Algorithm
# We calculate a basic Euclidean 'Match Score' (Lower distance = Better match)
def calculate_match_score(row):
    energy_diff = (row['energy_level'] - user_profile['preferred_energy']) ** 2
    kids_diff = (row['good_with_kids'] - user_profile['preferred_kid_friendly']) ** 2
    return (energy_diff + kids_diff) ** 0.5

# Apply our statistical algorithm across the dataset
df['match_distance'] = df.apply(calculate_match_score, axis=1)

# Sort by the closest mathematical match
matched_breeds = df.sort_values(by='match_distance')

# 4. Output the predictive results
print("\n🧬 Data Science Prediction Alert: Optimal matches calculated for user profile!")
print(f"Target Preferences -> Energy: {user_profile['preferred_energy']}, Kid-Friendly: {user_profile['preferred_kid_friendly']}\n")

# Display the top matches
for index, row in matched_breeds.iterrows():
    print(f"🐾 Breed: {row['breed_name_clean']} | Match Score (Lower is better): {row['match_distance']:.2f}")

conn.close()
