import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load data from the JSON file
data = pd.read_json('download.json')

# Check for missing values
if data.isnull().values.any():
    print("Warning: There are missing values in the dataset.")
    # You may choose to handle missing values here.

# Check data dimensions
if data.shape[0] == 0:
    print("Error: No samples left in the dataset after handling missing values.")
else:
    # Split the data into features (X) and target variables (y)
    X = data.drop(columns=['color_red', 'color_green', 'color_blue'])  # Features
    y = data[['color_red', 'color_green', 'color_blue']]  # Target variables

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Continue with your neural network training and evaluation

# Extract input parameters (X) and RGB color values (y)
X = data[['scanning_speed', 'average_power', 'scan_step', 'pulse_duration', 'pulse_repetition_rate']].values
y = data[['color_red', 'color_green', 'color_blue']].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale RGB values to the range [0, 1]
scaler = MinMaxScaler()
y_train_scaled = scaler.fit_transform(y_train)
y_test_scaled = scaler.transform(y_test)

# Create a neural network model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='sigmoid'))  # Output layer with 3 neurons for RGB values

# Compile the model
model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001))

# Train the model
model.fit(X_train, y_train_scaled, epochs=100, batch_size=32, verbose=2)

# Make predictions on the test set
predicted_rgb_scaled = model.predict(X_test)

# Inverse transform the scaled RGB predictions to the original range [0, 255]
predicted_rgb = scaler.inverse_transform(predicted_rgb_scaled)

# Calculate Mean Squared Error and R-squared (R2) Score
mse = mean_squared_error(y_test, predicted_rgb)
r2 = r2_score(y_test, predicted_rgb)

print(f"Mean Squared Error: {mse}")
print(f"R-squared (R2) Score: {r2}")
print(f"Predicted RGB Color (scaled): {predicted_rgb_scaled[0]}")
print(f"Predicted RGB Color (original): {predicted_rgb[0]}")
