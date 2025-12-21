# src/data_loader.py
"""
Data loading and preprocessing for Amazon QA project
"""

import pandas as pd
import numpy as np

def load_categories():
    """Load category mapping"""
    categories = pd.read_csv('data/raw/amazon_categories.csv')
    return categories

def load_sample_products(n_samples=1000):
    """
    Load sample products for analysis
    In production: Replace with actual data loading
    """
    # For now, create sample data
    sample_data = pd.DataFrame({
        'asin': [f'B00{i:06d}' for i in range(n_samples)],
        'title': [f'Product Title {i}' for i in range(n_samples)],
        'price': np.random.uniform(10, 500, n_samples),
        'category_id': np.random.randint(1, 50, n_samples),
        'reviews': [f'Review text for product {i}' for i in range(n_samples)]
    })
    return sample_data

if __name__ == "__main__":
    print("Data Loader Module")
    categories = load_categories()
    print(f"Loaded {len(categories)} categories")