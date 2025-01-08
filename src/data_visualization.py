import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('data/service_desk_cleaned.csv')

# Plot the distribution of resolution times
plt.figure(figsize=(10, 6))
sns.histplot(df['Resolution Time'], bins=20, kde=True)
plt.title('Distribution of Resolution Times')
plt.xlabel('Resolution Time (hours)')
plt.ylabel('Frequency')
plt.show()

# Plot the priority distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Priority_Medium', data=df, palette='Set2')
plt.title('Distribution of Ticket Priority')
plt.xlabel('Priority')
plt.ylabel('Count')
plt.show()

# Correlation heatmap of features and resolution time
plt.figure(figsize=(10, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
