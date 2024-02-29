import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
url = "https://gist.githubusercontent.com/tacksoo/12a8375579e574a77586830498a9a280/raw/bfdc3180e4f91da97e08d4ca5b62e45b32d7d7b8/experience.csv"
data = pd.read_csv(url)

# Extracting features and target variable
X = data[['YearsExperience']]
y = data['Salary']

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict salary for ten years of experience
years_of_experience = [[10]]
predicted_salary = model.predict(years_of_experience)

formatted_predicted_salary = "{:.2f}".format(predicted_salary[0])

print("Predicted salary for ten years of experience:", formatted_predicted_salary)