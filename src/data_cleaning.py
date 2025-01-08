import pandas as pd

# Load the dataset
df = pd.read_csv('data/service_desk_data.csv')

# Convert 'Creation Date' to datetime
df['Creation Date'] = pd.to_datetime(df['Creation Date'])

# Handle missing values (if any)
df.fillna(method='ffill', inplace=True)

# Convert 'Priority' and 'Issue Type' to categorical variables using one-hot encoding
df = pd.get_dummies(df, columns=['Priority', 'Issue Type'], drop_first=True)

# Save cleaned data
df.to_csv('data/service_desk_cleaned.csv', index=False)
