import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read the data
data = pd.read_csv('data/coupons.csv')

# Set the style and figure size
plt.style.use('default')
plt.figure(figsize=(10, 6))

# Create the histogram
sns.histplot(data=data, x='temperature', bins=3, stat='count')

# Add value labels on top of each bar
for i in plt.gca().patches:
    plt.gca().annotate(f'{int(i.get_height())}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

# Customize the plot
plt.title('Distribution of Temperature Values', fontsize=14, pad=20)
plt.xlabel('Temperature (°F)', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('temperature_distribution.png')
plt.close() 