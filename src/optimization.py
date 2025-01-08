import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('data/service_desk_cleaned.csv')

# Split the data into features (X) and target (y)
X = df.drop(['Resolution Time', 'Ticket ID', 'Creation Date', 'Status', 'Assigned Team'], axis=1)
y = df['Resolution Time']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the random forest regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict the resolution time on the test set
y_pred = rf_model.predict(X_test)

# Feature importance from the trained model
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("Feature Importance:\n", feature_importance)

# Plotting feature importance
plt.figure(figsize=(10, 6))
feature_importance.plot(kind='bar', x='Feature', y='Importance', legend=False)
plt.title('Feature Importance from Random Forest Model')
plt.ylabel('Importance')
plt.xlabel('Features')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
