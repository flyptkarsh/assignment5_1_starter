import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read the data
data = pd.read_csv('data/coupons.csv')

# Set the style for better visualization
plt.style.use('default')
plt.figure(figsize=(12, 6))

# Create the bar plot with a color palette
sns.countplot(data=data, x='coupon', palette='viridis')

# Customize the plot
plt.title('Distribution of Coupon Types', fontsize=14, pad=20)
plt.xlabel('Coupon Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of each bar
for i in plt.gca().patches:
    plt.gca().annotate(f'{int(i.get_height())}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('coupon_distribution.png')
plt.close() 