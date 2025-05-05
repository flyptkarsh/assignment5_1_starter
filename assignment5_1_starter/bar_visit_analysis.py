import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('data/coupons.csv')

# Create a DataFrame with just bar coupons
bar_coupons_df = data[data['coupon'] == 'Bar']

# Create groups based on bar visit frequency
# Convert bar visit frequency to numeric values for comparison
def convert_bar_visits(x):
    if x == 'never':
        return 0
    elif x == 'less1':
        return 0.5
    elif x == '1~3':
        return 2
    elif x == '4~8':
        return 6
    elif x == 'gt8':
        return 9
    else:
        return None

bar_coupons_df['bar_visits_numeric'] = bar_coupons_df['Bar'].apply(convert_bar_visits)

# Create two groups: frequent (more than 3 times) and infrequent (3 or fewer times)
bar_coupons_df['visit_frequency'] = bar_coupons_df['bar_visits_numeric'].apply(
    lambda x: 'More than 3 times' if x > 3 else '3 or fewer times'
)

# Calculate acceptance rates for each group
acceptance_rates = bar_coupons_df.groupby('visit_frequency')['Y'].agg(['count', 'mean']).round(3)
acceptance_rates.columns = ['Total Coupons', 'Acceptance Rate']

# Print the results
print("\nBar Coupon Acceptance by Visit Frequency:")
print("-" * 50)
print(acceptance_rates)
print("\nDetailed Statistics:")
print("-" * 50)
print(f"Infrequent visitors (≤3 times/month):")
print(f"Total coupons: {acceptance_rates.loc['3 or fewer times', 'Total Coupons']}")
print(f"Acceptance rate: {acceptance_rates.loc['3 or fewer times', 'Acceptance Rate']*100:.1f}%")
print(f"\nFrequent visitors (>3 times/month):")
print(f"Total coupons: {acceptance_rates.loc['More than 3 times', 'Total Coupons']}")
print(f"Acceptance rate: {acceptance_rates.loc['More than 3 times', 'Acceptance Rate']*100:.1f}%")

# Create visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=bar_coupons_df, x='visit_frequency', y='Y')

# Add value labels on top of bars
for i in plt.gca().patches:
    plt.gca().annotate(f'{i.get_height():.2%}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

plt.title('Bar Coupon Acceptance Rate by Visit Frequency')
plt.xlabel('Bar Visit Frequency')
plt.ylabel('Acceptance Rate')
plt.ylim(0, 1)

# Save the plot
plt.tight_layout()
plt.savefig('bar_visit_acceptance.png')
plt.close() 