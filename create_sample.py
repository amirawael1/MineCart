# create_sample.py - Create sample dataset for GitHub
import pandas as pd
import os

print("="*60)
print("CREATING SAMPLE DATASET FOR GITHUB")
print("="*60)

# Path to your full dataset (where you moved it)
full_data_path = r"C:\Users\Master\Desktop\amazon_products_full.csv"

# Check if file exists
if not os.path.exists(full_data_path):
    print(f"❌ ERROR: File not found at: {full_data_path}")
    print("\nPlease check the file exists at that location.")
    print("You moved it with this command:")
    print('  Move-Item "data\\raw\\amazon_products.csv" "C:\\Users\\Master\\Desktop\\amazon_products_full.csv"')
    exit(1)

print(f"✓ Found full dataset at: {full_data_path}")

# Load the full dataset
print("\n📥 Loading full dataset...")
try:
    full_data = pd.read_csv(full_data_path)
    print(f"✓ Loaded: {len(full_data):,} rows, {len(full_data.columns)} columns")
    
    # Show column names
    print(f"📋 Columns: {list(full_data.columns)}")
    
except Exception as e:
    print(f"❌ Error loading file: {e}")
    print("\nPossible issues:")
    print("1. File might be corrupted")
    print("2. Wrong file format (not CSV)")
    print("3. File is too large for memory")
    exit(1)

# Create sample (10,000 rows)
sample_size = min(10000, len(full_data))
print(f"\n🎯 Creating sample of {sample_size:,} rows...")

# Method 1: Random sample
sample_data = full_data.sample(n=sample_size, random_state=42)

# Method 2: If you want first N rows instead (faster)
# sample_data = full_data.head(sample_size)

print(f"✓ Sample created: {len(sample_data):,} rows")

# Save sample
output_path = "data/raw/amazon_products_sample.csv"
os.makedirs("data/raw", exist_ok=True)

sample_data.to_csv(output_path, index=False)
print(f"💾 Saved to: {output_path}")

# Create a tiny demo file too (100 rows)
demo_data = sample_data.head(100)
demo_data.to_csv("data/raw/amazon_products_demo.csv", index=False)
print(f"🔬 Demo file: data/raw/amazon_products_demo.csv (100 rows)")

print("\n" + "="*60)
print("✅ SAMPLE CREATION COMPLETE!")
print("="*60)
print(f"\n📊 STATISTICS:")
print(f"   Full dataset: {len(full_data):,} rows")
print(f"   GitHub sample: {len(sample_data):,} rows")
print(f"   Demo file: {len(demo_data):,} rows")

print("\n📁 FILE STRUCTURE:")
print("   data/raw/")
print("   ├── amazon_categories.csv      ← Your categories")
print("   ├── amazon_products_sample.csv ← 10K sample (for GitHub)")
print("   └── amazon_products_demo.csv   ← 100 rows (for quick tests)")

print("\n🚫 IMPORTANT:")
print("   • Full dataset: C:\\Users\\Master\\Desktop\\amazon_products_full.csv")
print("   • NEVER commit full dataset to GitHub!")
print("   • Only commit the sample files")