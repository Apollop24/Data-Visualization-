#install the required libraries

#pip install pandas
#pip install numpy
#pip install matplotlib
#pip install seaborn
#pip install geopandas matplotlib descartes



#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Specify the path to the dat in Excel file
csv_file_path = r"C:\Users\TOO\Downloads\HEATMAP\sales_record.csv"

# Read the Excel file into a pandas DataFrame
data = pd.read_csv(csv_file_path)

# View the imported data (optional)
print(data)



# Group the data by 'Country' and calculate the total profit for each country
profit_by_country = data.groupby('Country')['Total Profit'].sum().reset_index()
print(profit_by_country )

# Load the world countries shapefile

world = gpd.read_file('C:/Users/TOO/Downloads/WORLD/ne_50m_admin_0_countries.shp')
# Merge the profit_by_country DataFrame with the world shapefile based on the country name
merged_data = world.merge(profit_by_country, left_on='ADMIN', right_on='Country', how='left')

# Plot the geographical heatmap
fig, ax = plt.subplots(figsize=(12, 8))

# Ensure 'Total Profit' values are numeric (replace 'Total Profit' with the actual column name if needed)
merged_data['Total Profit'] = pd.to_numeric(merged_data['Total Profit'], errors='coerce')

# Plot the heatmap using 'Total Profit' column
merged_data.plot(column='Total Profit', cmap='coolwarm', linewidth=0.8, ax=ax, legend=True, legend_kwds={'label': 'Total Profit'})

# Add a title to the plot
plt.title('Geographical Heatmap of Total Profit by Country')

# Remove axis
ax.set_axis_off()

# Show the plot
plt.show()

























































































# Sample correlation matrix
correlation_matrix = np.array([[1.0, 0.8, 0.6],
                               [0.8, 1.0, 0.4],
                               [0.6, 0.4, 1.0]])

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.xlabel("Variables")
plt.ylabel("Variables")
plt.show()
