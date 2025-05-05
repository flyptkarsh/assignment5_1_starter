import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('data/coupons.csv')

# Create a DataFrame with just bar coupons
bar_coupons_df = data[data['coupon'] == 'Bar']

# Print basic information about the bar coupons
print("\nBar Coupon Analysis:")
print("-" * 50)
print(f"Total number of coupons in dataset: {len(data)}")
print(f"Number of bar coupons: {len(bar_coupons_df)}")
print(f"Percentage of bar coupons: {(len(bar_coupons_df) / len(data)) * 100:.2f}%")

# Save the bar coupons to a CSV file for further analysis
bar_coupons_df.to_csv('bar_coupons.csv', index=False)

# Create a simple visualization of bar coupon acceptance rate
plt.figure(figsize=(8, 6))
sns.countplot(data=bar_coupons_df, x='Y')

# Add value labels on top of bars
for i in plt.gca().patches:
    plt.gca().annotate(f'{int(i.get_height())}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

plt.title('Bar Coupon Acceptance Distribution')
plt.xlabel('Accepted (1) vs Rejected (0)')
plt.ylabel('Count')

# Save the plot
plt.tight_layout()
plt.savefig('bar_coupon_acceptance.png')
plt.close() 