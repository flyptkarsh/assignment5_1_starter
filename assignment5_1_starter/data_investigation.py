import pandas as pd
import numpy as np

# Read the data
data = pd.read_csv('data/coupons.csv')

# 1. Check for missing values
print("=== Missing Values Analysis ===")
missing_values = data.isnull().sum()
missing_percentage = (missing_values / len(data)) * 100

missing_analysis = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})

print("\nMissing values by column:")
print(missing_analysis[missing_analysis['Missing Values'] > 0].sort_values('Missing Values', ascending=False))

# 2. Check for data types and potential issues
print("\n=== Data Types Analysis ===")
print("\nData types of each column:")
print(data.dtypes)

# 3. Check for unique values in categorical columns
print("\n=== Categorical Columns Analysis ===")
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"\nUnique values in {col}:")
    print(data[col].value_counts())
    print(f"Number of unique values: {data[col].nunique()}")

# 4. Check for numerical columns
print("\n=== Numerical Columns Analysis ===")
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_columns:
    print(f"\nStatistics for {col}:")
    print(data[col].describe())

# 5. Check for potential data quality issues
print("\n=== Data Quality Issues ===")

# Check for inconsistent values in age
print("\nAge value distribution:")
print(data['age'].value_counts().sort_index())

# Check for inconsistent values in temperature
print("\nTemperature value distribution:")
print(data['temperature'].value_counts().sort_index())

# Check for inconsistent values in time
print("\nTime value distribution:")
print(data['time'].value_counts())

# Check for inconsistent values in weather
print("\nWeather value distribution:")
print(data['weather'].value_counts())

# Check for inconsistent values in coupon types
print("\nCoupon type distribution:")
print(data['coupon'].value_counts())

# 6. Check for potential duplicates
print("\n=== Duplicate Analysis ===")
duplicates = data.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")

# 7. Check for potential outliers in numerical columns
print("\n=== Outlier Analysis ===")
for col in numerical_columns:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)][col]
    print(f"\nPotential outliers in {col}: {len(outliers)}")
    if len(outliers) > 0:
        print(f"Outlier values: {outliers.unique()}") 