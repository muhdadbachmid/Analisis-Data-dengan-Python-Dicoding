Streamlit Dashboard for Data Analysis
Datasets Used
The following datasets are used in this project:

orders_dataset.csv: Contains order details, including timestamps for various stages of the order.
customers_dataset.csv: Contains customer information such as city and state.
geolocation_dataset.csv: Contains geographic information about the customers and sellers.
order_items_dataset.csv: Contains data on items ordered, including price and shipping details.
order_payments_dataset.csv: Contains payment methods and values.
order_reviews_dataset.csv: Contains customer reviews and review scores.
product_category_name_translation.csv: Contains product category translations.
sellers_dataset.csv: Contains seller details like city and state.
products_dataset.csv: Contains product details such as category and dimensions.
Features
Analyze Delivery Time & Customer Satisfaction: Visualize the relationship between delivery times and review scores.
Most Purchased Product Categories: Analyze the most purchased product categories and their corresponding seller performance based on location.
Prerequisites
To run this project, ensure that you have the following software installed:

Python 3.8+
pip (Python package manager)
Virtual environment (optional but recommended)

Running the Dashboard
Once all dependencies are installed and datasets are in place, run the Streamlit dashboard using the following command:

streamlit run dashboard.py
