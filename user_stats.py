"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""


import statistics as stats
# define a variable with some univariant data 

# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]


# Calculate the mean of the agility scores
mean = stats.mean(scores)
print(f'Mean: {mean}')

# Calculate the median of the agility scores
median = stats.median(scores)
print(f'Median: {median}')

# Calculate the mode of the agility scores
try:
    mode = stats.mode(scores)
    print(f'Mode: {mode}')
except stats.StatisticsError:
    print("There is no mode")

# Calculate the variance of the agility scores
variance = stats.pvariance(scores)
print(f'Variance: {variance}')

# Calculate the standard deviation of the agility scores
stdev = stats.pstdev(scores)
print(f'Standard deviation: {stdev}')

# create and fit the linear regression model
reg = LinearRegression()
reg.fit(x_times.reshape(-1, 1), y_temps)

# calculate slope and intercept of best fit line 
slope = reg.coef_
intercept = reg.intercept_
print(f'Slope: {slope}, Intercept: {intercept}')

# predict future temperature
x_future = 13
y_future = reg.predict([[x_future]])
print(f'Temperature at {x_future} hour: {y_future}')
