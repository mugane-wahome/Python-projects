
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
data = pd.read_csv("pollution.csv")

print(data.head())

                      date  pollution  dew  temp   press wnd_dir  wnd_spd  snow  \
    0  2010-01-02 00:00:00      129.0  -16  -4.0  1020.0      SE     1.79     0   
    1  2010-01-02 01:00:00      148.0  -15  -4.0  1020.0      SE     2.68     0   
    2  2010-01-02 02:00:00      159.0  -11  -5.0  1021.0      SE     3.57     0   
    3  2010-01-02 03:00:00      181.0   -7  -5.0  1022.0      SE     5.36     1   
    4  2010-01-02 04:00:00      138.0   -7  -5.0  1022.0      SE     6.25     2   
    
       rain  
    0     0  
    1     0  
    2     0  
    3     0  
    4     0  
    
variables = data.columns
observations = data.shape

print(variables)
print(observations)

    Index(['date', 'pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd',
           'snow', 'rain'],
          dtype='object')
    (43800, 9)
    
# Define the target variable (dependent variable)
target_variable = 'temp'
# Define the independent variables (features)
independent_variables = ['dew', 'press', 'wnd_spd', 'snow', 'rain', 'pollution']

# Split data  into training and testing sets (test_size is the proportion for testing data)
X_train, X_test, y_train, y_test = train_test_split(data[independent_variables], data[target_variable], test_size=0.2, random_state=42)

# Creating a linear regression model
model = LinearRegression()
# Fit the model to the training data
model.fit(X_train, y_train)
# Predict temperature values for the testing data
y_pred = model.predict(X_test)

# Calculate mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate R-squared value
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared:", r2)

    Mean Squared Error: 28.56838707357901
    R-squared: 0.8053708717225844
    
# Print the coefficients of the model
print("Coefficients:", model.coef_)

# Print the intercept of the model
print("Intercept:", model.intercept_)


    Coefficients: [ 0.46092645 -0.49855462  0.010065   -0.69520541 -0.54284666 -0.02509022]
    Intercept: 520.6197143976284
