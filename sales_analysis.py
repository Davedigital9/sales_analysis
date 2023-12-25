import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
file_path = r'C:\Users\HP\Desktop\sales_dataset\supermarket_sales - Sheet1.csv'
sales_data = pd.read_csv(file_path)

# Display basic information about the dataset
print(sales_data.info())

# Display the first few rows of the dataset
print(sales_data.head())

# Calculate total sales per product
total_sales_per_product = sales_data.groupby('Product line')['Total'].sum()

# Plot a bar chart of total sales per product
total_sales_per_product.plot(kind='bar', xlabel='Product Line', ylabel='Total Sales', title='Total Sales per Product Line')
plt.show()

# Calculate and plot monthly sales trends
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
monthly_sales = sales_data.resample('M', on='Date')['Total'].sum()

monthly_sales.plot(xlabel='Date', ylabel='Total Sales', title='Monthly Sales Trends')
plt.show()