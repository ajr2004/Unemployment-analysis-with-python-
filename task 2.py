import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Install Plotly if not already installed
!pip install plotly

# Read the data from CSV files
data = pd.read_csv('Unemp_in_India.csv')
data = pd.read_csv('Unemp_Rate_upto_11_2020.csv')

# Print information about the data
print(data.info())

# Rename columns for better understanding
data.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment rate',
                'Estimated Employed', 'Estimated Labour participation rate',
                'Region', 'Longitude', 'Latitude']

# Explore the dataset
print(data.head(10))
print("\nDescriptive statistics of the dataset:")
print(data.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Heatmap to visualize the correlation between columns
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Histogram - Estimated Employed with hue (Region)
sns.histplot(x='Estimated Employed', hue='Region', data=data)
plt.title('Estimated Employed')
plt.show()

# Histogram - Estimated Unemployment rate with hue (States)
sns.histplot(x='Estimated Unemployment rate', hue='States', data=data)
plt.title("Estimated Unemployment rate")
plt.show()

# Histogram - Estimated Unemployment rate with hue (Region)
sns.histplot(x='Estimated Unemployment rate', hue='Region', data=data)
plt.title('Unemployment rate')
plt.show()

# Creating a dashboard to analyze the unemployment rate of each Indian state by region using Plotly Sunburst chart
unemployment = data[['States', 'Region', 'Estimated Unemployment rate']]
figure = px.sunburst(unemployment, path=['States', 'Region'], values='Estimated Unemployment rate',
                     width=1000, height=1000, color_continuous_scale='RdYlGn',
                     title='Unemployment Rate in India (Dashboard to analyze the unemployment rate)')
figure.show()
