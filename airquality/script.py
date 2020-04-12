# import packages
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# import dataset from R lang
!pip install pydataset
from pydataset import data as ds

# Set data as DataFrame
data = pd.DataFrame(ds('airquality'))
data.head()

# drop unnecessary columns
data.drop(['Month', 'Day'], axis=1, inplace=True)
data.head()

# drop missing values
data.dropna(inplace=True)
data.head()

def plot_scatter(x, y, x_title, y_title):
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  ax.scatter(x, y)

  ax.set_title('Testify linearlity between %s and %s' % (y_title, x_title))
  ax.set_xlabel(x_title)
  ax.set_ylabel(y_title)

  fig.show()

# Extract variables
variables = data.columns
endog_title = variables[0]
exog_titles = variables[1:]

# Plot scatter
endog = data[endog_title]
for exog_title in exog_titles:
  exog = data[exog_title]
  plot_scatter(exog, endog, exog_title, endog_title)

#OLS
y = data[data.columns[1]]
X = data[data.columns[2:]]

# Add constant
X = sm.add_constant(X)

# Fit regression model
results = sm.OLS(y, X).fit()

# Inspect the results
print(results.summary())
