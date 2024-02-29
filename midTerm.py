from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame from the data
df = pd.read_csv("https://gist.githubusercontent.com/tacksoo/3f35786024778a4bbb5197bbd224e57e/raw/f19ff22314bc6cf6d69d89cd61e7648f07649ab6/temperature.csv")

# Train a linear regression model
X = df[['Temperature']]
y = df['CanPlay']
model = LinearRegression()
model.fit(X, y)

# Predict the action for temperature 77 degrees
temperature_to_predict = 77


predicted_action = model.predict([[temperature_to_predict]])[0]

# Print the predicted action
if predicted_action > 0.5:
    print("You can play outside!")
else:
    print("Sorry, you can't play outside.")