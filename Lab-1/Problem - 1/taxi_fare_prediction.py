import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample dataset (10 records)
data = {
    'trip_miles': [1.2, 3.5, 2.0, 5.1, 0.8, 4.2, 3.0, 6.3, 2.5, 1.0],
    'pickup_community_area': [8, 32, 12, 18, 5, 23, 14, 30, 6, 7],
    'dropoff_community_area': [10, 40, 15, 25, 5, 20, 12, 28, 8, 7],
    'fare': [6.5, 14.2, 9.0, 18.6, 5.2, 16.3, 11.0, 22.5, 10.1, 7.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['trip_miles', 'pickup_community_area', 'dropoff_community_area']]
y = df['fare']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Output
print("\n--- Taxi Fare Prediction (Sample Data) ---")
print(f"Intercept: {model.intercept_:.2f}")
print("Coefficients:")
print(f"  trip_miles: {model.coef_[0]:.2f}")
print(f"  pickup_community_area: {model.coef_[1]:.2f}")
print(f"  dropoff_community_area: {model.coef_[2]:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print("------------------------------------------")

# Plot: Actual vs Predicted
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Ideal Fit')
plt.xlabel('Actual Fare')
plt.ylabel('Predicted Fare')
plt.title('Actual vs Predicted Taxi Fare')
plt.legend()
plt.tight_layout()

# Save to current folder
plot_filename = "fare_prediction_plot.png"
plt.savefig(plot_filename)
print(f" Graph saved as: {os.path.abspath(plot_filename)}")

# Optional: Show the plot
plt.show()
