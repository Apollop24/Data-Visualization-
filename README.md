

# Sales Data Analysis and Visualization

This repository contains scripts for analyzing and visualizing sales data for a private company. The analysis includes generating a geographical heatmap of total profit by country and creating a sample correlation heatmap.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Source](#data-source)
3. [Installation](#installation)
4. [Data Preparation](#data-preparation)
5. [Attribute Information](#attribute-information)
6. [Geographical Heatmap](#geographical-heatmap)
7. [Correlation Heatmap](#correlation-heatmap)
8. [Conclusion](#conclusion)

## Introduction

This project aims to analyze and visualize sales data for a private company. The analysis includes calculating the total profit by country and visualizing it on a geographical heatmap. Additionally, a sample correlation heatmap is created to show the relationships between different variables.

## Data Source

The data used in this project is a sales record dataset with the following attributes:

## Attribute Information

- **Region**: Geographic region where the sale occurred
- **Country**: Country where the sale occurred
- **Item Type**: Type of item sold
- **Sales Channel**: Channel through which the sale was made (e.g., online, offline)
- **Order Priority**: Priority of the order (e.g., high, medium, low)
- **Order Date**: Date when the order was placed
- **Order ID**: Unique identifier for the order
- **Ship Date**: Date when the order was shipped
- **Units Sold**: Number of units sold
- **Unit Price**: Price per unit
- **Unit Cost**: Cost per unit
- **Total Revenue**: Total revenue generated from the sale
- **Total Cost**: Total cost incurred for the sale
- **Total Profit**: Total profit generated from the sale

## Installation

Ensure you have the following Python libraries installed:
```bash
pip install pandas numpy matplotlib seaborn geopandas
```

## Data Preparation

Load the required libraries and read the data from the CSV file:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Load data
csv_file_path = r"C:\Users\TOO\Downloads\HEATMAP\sales_record.csv" 
data = pd.read_csv(csv_file_path)
```

## Geographical Heatmap

To create a geographical heatmap of total profit by country, follow these steps:

1. Group the data by 'Country' and calculate the total profit:
   ```python
   profit_by_country = data.groupby('Country')['Total Profit'].sum().reset_index()
   ```

2. Load the world countries shapefile:
   ```python
   world = gpd.read_file('C:/Users/TOO/Downloads/WORLD/ne_50m_admin_0_countries.shp')
   ```

3. Merge the profit data with the world shapefile on the country name:
   ```python
   merged_data = world.merge(profit_by_country, left_on='ADMIN', right_on='Country', how='left')
   ```

4. Create the geographical heatmap:
   ```python
   fig, ax = plt.subplots(figsize=(12, 8))
   merged_data['Total Profit'] = pd.to_numeric(merged_data['Total Profit'], errors='coerce') 
   merged_data.plot(column='Total Profit', cmap='coolwarm', linewidth=0.8, ax=ax, legend=True, legend_kwds={'label': 'Total Profit'})
   plt.title('Geographical Heatmap of Total Profit by Country')  
   ax.set_axis_off() 
   plt.show()
   ```

## Correlation Heatmap

To create a sample correlation heatmap, follow these steps:

1. Create a sample correlation matrix:
   ```python
   correlation_matrix = np.array([[1.0, 0.8, 0.6], [0.8, 1.0, 0.4], [0.6, 0.4, 1.0]])
   ```

2. Create the correlation heatmap:
   ```python
   plt.figure(figsize=(8, 6))
   sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
   plt.title("Correlation Heatmap")
   plt.xlabel("Variables")
   plt.ylabel("Variables")
   plt.show()
   ```

## Conclusion

This project demonstrates how to analyze and visualize sales data using Python. The geographical heatmap provides insights into the total profit by country, while the correlation heatmap shows the relationships between different variables. These visualizations can help in making data-driven decisions for the company.




This README file provides a comprehensive guide for the project, including all necessary steps and information.
