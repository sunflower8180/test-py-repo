import pandas as pd
from fuzzywuzzy import fuzz, process

# Sample CRM Data
data = {
    'Customer_ID': [1, 2, 3, 4, 5],
    'Name': ['John Doe', 'Jon Doe', 'Jane Smith', 'Jane Smithe', 'Mike Johnson'],
    'Email': ['john.doe@example.com', 'johnd@example.com', 'jane.smith@example.com', 
              'jane.s@example.com', 'mike.j@example.com'],
    'Phone': ['123-456-7890', '1234567890', '987-654-3210', '9876543210', '555-123-4567']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to find duplicate records based on name similarity
def find_duplicates(df, column, threshold=85):
    duplicates = []
    for i, name in enumerate(df[column]):
        match, score = process.extractOne(name, df[column])
        if score > threshold and name != match:
            duplicates.append((name, match, score))
    return duplicates

# Detect duplicate records
duplicate_records = find_duplicates(df, 'Name')

# Output duplicate records
print("Potential Duplicate Records:")
for record in duplicate_records:
    print(f"{record[0]} <-> {record[1]} (Similarity: {record[2]}%)")