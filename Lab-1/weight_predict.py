import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Weight': [79, 69, 73, 95, 82, 55, 69, 71, 64, 69],
    'Height': [1.80, 1.68, 1.82, 1.70, 1.87, 1.55, 1.50, 1.78, 1.67, 1.64],
    'Age': [35, 39, 25, 60, 27, 18, 89, 42, 16, 52],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode Gender: Male = 1, Female = 0
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Define inputs and output
X = df[['Height', 'Age', 'Gender']]
y = df['Weight']

# Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Output coefficients
print("\n--- Linear Regression Model Results ---")
print(f"Intercept: {model.intercept_:.2f}")
print("Coefficients:")
print(f"  Height: {model.coef_[0]:.2f}")
print(f"  Age:    {model.coef_[1]:.2f}")
print(f"  Gender: {model.coef_[2]:.2f}")

# Predict sample
sample = [[1.75, 30, 1]]  # Height, Age, Gender (Male)
pred = model.predict(sample)
print(f"\nPredicted Weight for [1.75m, 30yrs, Male]: {pred[0]:.2f} kg")
print("-----------------------------------------\n")
