
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load combined dataset
df_all = pd.read_csv('C:\\Users\\91996\\Desktop\\New folder\\.vscode\\Python\\Projects\\Car Price Preditor\\archive\\combined_car_data.csv')  # replace with your combined CSV file

# Select useful columns
useful_cols = [
    'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven',
    'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'
]
df = df_all[useful_cols]

# Drop rows with missing values in selected columns
df = df.dropna()

# Feature engineering: create 'Age' from 'Year'
current_year = 2025
df['Age'] = current_year - df['Year']

# Drop 'Year' (optional since Age covers it)
df = df.drop(columns=['Year'])

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['Fuel_Type', 'Seller_Type', 'Transmission'], drop_first=True)

# Separate features and target
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Test MSE: {mse:.3f}")
print(f"Test R²: {r2:.3f}")

# Save model and feature columns
joblib.dump(model, 'car_price_model.pkl')
joblib.dump(X.columns.tolist(), 'car_features.pkl')

print("Model and features saved successfully!")



