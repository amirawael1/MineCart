# report_generator.py - Generate Milestone 1 reports
import pandas as pd
import numpy as np
import os
from datetime import datetime

print("📊 GENERATING MILESTONE 1 REPORTS")
print("="*50)

# Create reports folder
os.makedirs('reports', exist_ok=True)

# Load data
print("Loading data...")
categories = pd.read_csv('data/raw/amazon_categories.csv')
products = pd.read_csv('data/raw/amazon_products_sample.csv')
data = products.merge(categories, left_on='category_id', right_on='id')

print(f"Data loaded: {len(data):,} rows")

# 1. Create analysis summary
print("\n1. Creating analysis summary...")
summary = {
    'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'total_products': len(data),
    'total_columns': len(data.columns),
    'missing_values_total': int(data.isnull().sum().sum()),
    'unique_categories': data['category_name'].nunique(),
    'avg_price': float(data['price'].mean()) if 'price' in data.columns else None,
    'min_price': float(data['price'].min()) if 'price' in data.columns else None,
    'max_price': float(data['price'].max()) if 'price' in data.columns else None,
    'products_with_reviews': int(data['reviews'].notnull().sum()) if 'reviews' in data.columns else None,
    'best_seller_count': int(data['isBestSeller'].sum()) if 'isBestSeller' in data.columns else None,
    'data_source': 'GitHub Sample (10,000 rows)'
}

summary_df = pd.DataFrame([summary])
summary_path = 'reports/milestone1_analysis_summary.csv'
summary_df.to_csv(summary_path, index=False)
print(f"   ✓ Saved: {summary_path}")

# 2. Create category distribution
print("\n2. Creating category distribution...")
if 'category_name' in data.columns:
    cat_dist = data['category_name'].value_counts().reset_index()
    cat_dist.columns = ['category', 'count']
    cat_dist['percentage'] = (cat_dist['count'] / len(data) * 100).round(2)
    cat_path = 'reports/category_distribution.csv'
    cat_dist.to_csv(cat_path, index=False)
    print(f"   ✓ Saved: {cat_path}")
    
    print(f"\n   Top 5 categories:")
    for i, row in cat_dist.head(5).iterrows():
        print(f"   {i+1}. {row['category']}: {row['count']} products ({row['percentage']}%)")

# 3. Create price statistics
print("\n3. Creating price statistics...")
if 'price' in data.columns:
    price_stats = data['price'].describe().reset_index()
    price_stats.columns = ['statistic', 'value']
    price_path = 'reports/price_statistics.csv'
    price_stats.to_csv(price_path, index=False)
    print(f"   ✓ Saved: {price_path}")

# 4. Create missing values report
print("\n4. Creating missing values report...")
missing = data.isnull().sum().reset_index()
missing.columns = ['column', 'missing_count']
missing['missing_percentage'] = (missing['missing_count'] / len(data) * 100).round(2)
missing = missing[missing['missing_count'] > 0]
missing_path = 'reports/missing_values.csv'
missing.to_csv(missing_path, index=False)
print(f"   ✓ Saved: {missing_path}")

print("\n" + "="*50)
print("✅ REPORTS GENERATED SUCCESSFULLY!")
print("="*50)

print("\n📁 Files in reports/ folder:")
for file in os.listdir('reports'):
    print(f"   • {file}")

print("\n📋 Quick Summary:")
print(f"   Total Products: {len(data):,}")
print(f"   Categories: {data['category_name'].nunique()}")
if 'price' in data.columns:
    print(f"   Average Price: ${data['price'].mean():.2f}")
print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
