# Install required libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Load data
# Specify path to CSV file
csv_file_path = r"C:\Users\TOO\Downloads\HEATMAP\sales_record.csv" 

# Read CSV into pandas DataFrame
data = pd.read_csv(csv_file_path)

# Group data by 'Country' and calculate total profit 
profit_by_country = data.groupby('Country')['Total Profit'].sum().reset_index()

# Load world countries shapefile
world = gpd.read_file('C:/Users/TOO/Downloads/WORLD/ne_50m_admin_0_countries.shp')

# Merge profit data with world shapefile on country name
merged_data = world.merge(profit_by_country, left_on='ADMIN', right_on='Country', how='left')

# Create geographic heatmap 
fig, ax = plt.subplots(figsize=(12, 8))
merged_data['Total Profit'] = pd.to_numeric(merged_data['Total Profit'], errors='coerce') 
merged_data.plot(column='Total Profit', cmap='coolwarm', linewidth=0.8, ax=ax, legend=True, legend_kwds={'label': 'Total Profit'})

# Add plot title and remove axes
plt.title('Geographical Heatmap of Total Profit by Country')  
ax.set_axis_off() 

# Show plot
plt.show()

# Create sample correlation matrix
correlation_matrix = np.array([[1.0, 0.8, 0.6], [0.8, 1.0, 0.4], [0.6, 0.4, 1.0]])

# Create correlation heatmap 
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.xlabel("Variables")
plt.ylabel("Variables")
plt.show()
