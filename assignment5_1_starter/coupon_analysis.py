import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Read the data
data = pd.read_csv('data/coupons.csv')

# 2. Investigate missing data
print("\nMissing values in each column:")
print(data.isnull().sum())

# 3. Handle missing data
# For this analysis, we'll drop rows with missing values since they're relatively few
data_cleaned = data.dropna()

# 4. Calculate proportion of accepted coupons
total_observations = len(data_cleaned)
accepted_coupons = data_cleaned['Y'].sum()
acceptance_rate = accepted_coupons / total_observations

print(f"\nTotal observations: {total_observations}")
print(f"Accepted coupons: {accepted_coupons}")
print(f"Acceptance rate: {acceptance_rate:.2%}")

# 5. Bar plot of coupon types
plt.figure(figsize=(12, 6))
coupon_counts = data_cleaned['coupon'].value_counts()
sns.barplot(x=coupon_counts.index, y=coupon_counts.values)
plt.title('Distribution of Coupon Types')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/coupon_distribution.png')
plt.close()

# 6. Histogram of temperature
plt.figure(figsize=(10, 6))
sns.histplot(data=data_cleaned, x='temperature', bins=3)
plt.title('Distribution of Temperature')
plt.xlabel('Temperature (°F)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('images/temperature_distribution.png')
plt.close()

# Bar coupon analysis
bar_coupons = data_cleaned[data_cleaned['coupon'] == 'Bar'].copy()

# Calculate bar coupon acceptance rate
bar_acceptance_rate = bar_coupons['Y'].mean()
print(f"\nBar coupon acceptance rate: {bar_acceptance_rate:.2%}")

# Compare acceptance rates for bar frequency
bar_coupons['Bar'] = bar_coupons['Bar'].map({
    'never': 0,
    'less1': 0.5,
    '1~3': 2,
    '4~8': 6,
    'gt8': 9
})

frequent_bar_goers = bar_coupons[bar_coupons['Bar'] > 3]
infrequent_bar_goers = bar_coupons[bar_coupons['Bar'] <= 3]

print("\nBar coupon acceptance rates:")
print(f"Frequent bar goers (>3 times/month): {frequent_bar_goers['Y'].mean():.2%}")
print(f"Infrequent bar goers (≤3 times/month): {infrequent_bar_goers['Y'].mean():.2%}")

# Compare acceptance rates for age and bar frequency
bar_coupons['age'] = pd.to_numeric(bar_coupons['age'], errors='coerce')
frequent_and_older = bar_coupons[(bar_coupons['Bar'] > 1) & (bar_coupons['age'] > 25)]
others = bar_coupons[~((bar_coupons['Bar'] > 1) & (bar_coupons['age'] > 25))]

print("\nAge and bar frequency comparison:")
print(f"Frequent bar goers over 25: {frequent_and_older['Y'].mean():.2%}")
print(f"All others: {others['Y'].mean():.2%}")

# Compare acceptance rates for specific conditions
specific_group = bar_coupons[
    (bar_coupons['Bar'] > 1) & 
    (bar_coupons['passanger'] != 'Kid(s)') & 
    (~bar_coupons['occupation'].isin(['Farming Fishing & Forestry']))
]
other_group = bar_coupons[~(
    (bar_coupons['Bar'] > 1) & 
    (bar_coupons['passanger'] != 'Kid(s)') & 
    (~bar_coupons['occupation'].isin(['Farming Fishing & Forestry']))
)]

print("\nSpecific conditions comparison:")
print(f"Frequent bar goers, no kids, not farming: {specific_group['Y'].mean():.2%}")
print(f"All others: {other_group['Y'].mean():.2%}")

# Compare multiple conditions
group1 = bar_coupons[
    (bar_coupons['Bar'] > 1) & 
    (bar_coupons['passanger'] != 'Kid(s)') & 
    (bar_coupons['maritalStatus'] != 'Widowed')
]

group2 = bar_coupons[
    (bar_coupons['Bar'] > 1) & 
    (bar_coupons['age'] < 30)
]

# Convert RestaurantLessThan20 to numeric values
bar_coupons['RestaurantLessThan20'] = bar_coupons['RestaurantLessThan20'].map({
    'never': 0,
    'less1': 0.5,
    '1~3': 2,
    '4~8': 6,
    'gt8': 9
})

group3 = bar_coupons[
    (bar_coupons['RestaurantLessThan20'] > 4) & 
    (bar_coupons['income'].isin(['Less than $12500', '$12500 - $24999', '$25000 - $37499', '$37500 - $49999']))
]

print("\nMultiple conditions comparison:")
print(f"Group 1 (frequent bar, no kids, not widowed): {group1['Y'].mean():.2%}")
print(f"Group 2 (frequent bar, under 30): {group2['Y'].mean():.2%}")
print(f"Group 3 (frequent cheap restaurants, income < 50K): {group3['Y'].mean():.2%}")

# Independent investigation - Coffee House coupons
coffee_coupons = data_cleaned[data_cleaned['coupon'] == 'Coffee House']

# Analyze coffee house coupon acceptance by time of day
coffee_by_time = coffee_coupons.groupby('time')['Y'].mean()
print("\nCoffee House coupon acceptance by time of day:")
print(coffee_by_time)

# Visualize coffee house acceptance by time
plt.figure(figsize=(10, 6))
sns.barplot(x=coffee_by_time.index, y=coffee_by_time.values)
plt.title('Coffee House Coupon Acceptance by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Acceptance Rate')
plt.tight_layout()
plt.savefig('images/coffee_time_analysis.png')
plt.close()

# Analyze coffee house acceptance by weather
coffee_by_weather = coffee_coupons.groupby('weather')['Y'].mean()
print("\nCoffee House coupon acceptance by weather:")
print(coffee_by_weather)

# Visualize coffee house acceptance by weather
plt.figure(figsize=(10, 6))
sns.barplot(x=coffee_by_weather.index, y=coffee_by_weather.values)
plt.title('Coffee House Coupon Acceptance by Weather')
plt.xlabel('Weather')
plt.ylabel('Acceptance Rate')
plt.tight_layout()
plt.savefig('images/coffee_weather_analysis.png')
plt.close() 