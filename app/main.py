import pandas as pd

# Load data from the CSV file
data = pd.read_csv('orders.csv')

# Convert order_date to datetime and extract month and year
data['order_date'] = pd.to_datetime(data['order_date'])
data['month_year'] = data['order_date'].dt.to_period('M')

# Calculate monthly total revenue
monthly_revenue = data.groupby('month_year').agg(total_revenue=('product_price', lambda x: (x * data.loc[x.index, 'quantity']).sum())).reset_index()

# Calculate total revenue per product
product_revenue = data.groupby('product_id').agg(total_revenue=('product_price', lambda x: (x * data.loc[x.index, 'quantity']).sum())).reset_index()

# total revenue per customer
customer_revenue = data.groupby('customer_id').agg(total_revenue=('product_price', lambda x: (x * data.loc[x.index, 'quantity']).sum())).reset_index()

# top 10 customers by total revenue
top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(10)

# Output the results
print("Monthly Revenue:")
print(monthly_revenue)
print("\nProduct Revenue:")
print(product_revenue)
print("\nCustomer Revenue:")
print(customer_revenue)
print("\nTop 10 Customers by Revenue:")
print(top_customers)
