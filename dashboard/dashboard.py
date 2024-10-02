import streamlit as st
import pandas as pd

#Load ds
orders = pd.read_csv('orders_dataset.csv')
reviews = pd.read_csv('order_reviews_dataset.csv')
products = pd.read_csv('products_dataset.csv')
order_items = pd.read_csv('order_items_dataset.csv')
sellers = pd.read_csv('sellers_dataset.csv')
geolocation = pd.read_csv('geolocation_dataset.csv')
product_categories = pd.read_csv('product_category_name_translation.csv')

#Convert
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
reviews['review_answer_timestamp'] = pd.to_datetime(reviews['review_answer_timestamp'])

merged_data = pd.merge(orders, reviews, on='order_id')
merged_data['delivery_time'] = (merged_data['order_delivered_customer_date'] - merged_data['order_purchase_timestamp']).dt.days

#Title
st.title('E-Commerce Dashboard')

#Q1 Hubungan antara waktu pengiriman dan kepuasan pelanggan
st.header('Hubungan antara Waktu Pengiriman dan Kepuasan Pelanggan')
st.subheader('Rata-rata waktu pengiriman berdasarkan skor ulasan')

avg_delivery_time_per_score = merged_data.groupby('review_score')['delivery_time'].mean()

st.bar_chart(avg_delivery_time_per_score)

#Q2 Kategori produk yang paling banyak dibeli dan kinerja penjual berdasarkan lokasi
st.header('Kategori Produk Paling Banyak Dibeli dan Kinerja Penjual')

product_items_merged = pd.merge(order_items, products, on='product_id')
product_items_merged = pd.merge(product_items_merged, product_categories, on='product_category_name')

category_counts = product_items_merged['product_category_name_english'].value_counts().head(10)

st.subheader('Kategori Produk Paling Banyak Dibeli')
st.bar_chart(category_counts)

seller_items_merged = pd.merge(order_items, sellers, on='seller_id')
seller_items_merged = pd.merge(seller_items_merged, geolocation, left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix')

seller_performance = seller_items_merged.groupby(['geolocation_city', 'geolocation_state'])['order_item_id'].count().sort_values(ascending=False).head(10)

st.subheader('Kinerja Penjual Berdasarkan Lokasi (Top 10)')
st.table(seller_performance)
