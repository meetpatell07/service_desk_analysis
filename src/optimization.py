import pandas as pd

# Load cleaned data
df = pd.read_csv('data/service_desk_cleaned.csv')

# Use the trained model to get feature importances (if using RandomForest or similar)
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Feature importance
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("Feature Importance:\n", feature_importance)
