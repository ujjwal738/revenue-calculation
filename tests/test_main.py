import unittest
import pandas as pd
from io import StringIO

class TestRevenueCalculations(unittest.TestCase):

    def setUp(self):
        sample_data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
        1,101,2023-01-15,1001,Product A,10.0,2
        2,102,2023-01-18,1002,Product B,20.0,1
        3,103,2023-02-05,1001,Product A,10.0,1
        4,101,2023-02-20,1003,Product C,30.0,3
        5,104,2023-03-12,1002,Product B,20.0,2"""
        self.df = pd.read_csv(StringIO(sample_data))
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['month_year'] = self.df['order_date'].dt.to_period('M')

    def test_monthly_revenue(self):
        monthly_revenue = self.df.groupby('month_year').agg(total_revenue=('product_price', lambda x: (x * self.df.loc[x.index, 'quantity']).sum())).reset_index()
        expected = pd.DataFrame({'month_year': ['2023-01', '2023-02', '2023-03'], 'total_revenue': [40.0, 100.0, 40.0]})
        pd.testing.assert_frame_equal(monthly_revenue, expected)

    def test_product_revenue(self):
        product_revenue = self.df.groupby('product_id').agg(total_revenue=('product_price', lambda x: (x * self.df.loc[x.index, 'quantity']).sum())).reset_index()
        expected = pd.DataFrame({'product_id': [1001, 1002, 1003], 'total_revenue': [30.0, 60.0, 90.0]})
        pd.testing.assert_frame_equal(product_revenue, expected)

    def test_customer_revenue(self):
        customer_revenue = self.df.groupby('customer_id').agg(total_revenue=('product_price', lambda x: (x * self.df.loc[x.index, 'quantity']).sum())).reset_index()
        expected = pd.DataFrame({'customer_id': [101, 102, 103, 104], 'total_revenue': [90.0, 20.0, 10.0, 40.0]})
        pd.testing.assert_frame_equal(customer_revenue, expected)

    def test_top_customers(self):
        customer_revenue = self.df.groupby('customer_id').agg(total_revenue=('product_price', lambda x: (x * self.df.loc[x.index, 'quantity']).sum())).reset_index()
        top_customers = customer_revenue.nlargest(10, 'total_revenue')
        expected = pd.DataFrame({'customer_id': [101, 104, 102, 103], 'total_revenue': [90.0, 40.0, 20.0, 10.0]})
        pd.testing.assert_frame_equal(top_customers.reset_index(drop=True), expected)

if __name__ == '__main__':
    unittest.main()
