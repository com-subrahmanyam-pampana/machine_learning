import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Simulated dataset of houses (area in square feet, number of rooms, and house price)
data = {
    'Area': [1500, 1800, 2400, 3000, 3500, 4000, 5000],
    'Num_Rooms': [3, 4, 3, 5, 5, 6, 6],
    'Price': [400000, 500000, 600000, 700000, 800000, 850000, 950000]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df[['Area', 'Num_Rooms']]  # Features: Area and Number of Rooms
y = df['Price']  # Target: Price

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the house prices on the test set
y_pred = model.predict(X_test)

# Print the predictions and actual values
print("Predicted Prices:", y_pred)
print("Actual Prices:", y_test.values)

# Calculate Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualize the results (Area vs Price)
plt.scatter(df['Area'], df['Price'], color='blue', label='Actual prices')
plt.plot(X_test['Area'], y_pred, color='red', label='Predicted prices')
plt.xlabel('Area (Square Feet)')
plt.ylabel('Price ($)')
plt.title('House Price Prediction')
plt.legend()
plt.show()
