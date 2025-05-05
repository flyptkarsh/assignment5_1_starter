import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('data/coupons.csv')

# Create a DataFrame with just coffee house coupons
coffee_coupons_df = data[data['coupon'] == 'Coffee House'].copy()

# Convert coffee house visit frequency to numeric values
def convert_coffee_visits(x):
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

coffee_coupons_df['coffee_visits_numeric'] = coffee_coupons_df['CoffeeHouse'].apply(convert_coffee_visits)

# Create visit frequency groups
coffee_coupons_df['visit_frequency'] = coffee_coupons_df['coffee_visits_numeric'].apply(
    lambda x: 'More than 3 times' if x > 3 else '3 or fewer times'
)

# Calculate acceptance rates by different characteristics
print("\nCoffee House Coupon Analysis:")
print("-" * 50)
print(f"Total number of coffee house coupons: {len(coffee_coupons_df)}")

# 1. Acceptance by visit frequency
visit_acceptance = coffee_coupons_df.groupby('visit_frequency')['Y'].agg(['count', 'mean']).round(3)
visit_acceptance.columns = ['Total Coupons', 'Acceptance Rate']
print("\nAcceptance by Visit Frequency:")
print(visit_acceptance)

# 2. Acceptance by time of day
time_acceptance = coffee_coupons_df.groupby('time')['Y'].agg(['count', 'mean']).round(3)
time_acceptance.columns = ['Total Coupons', 'Acceptance Rate']
print("\nAcceptance by Time of Day:")
print(time_acceptance)

# 3. Acceptance by weather
weather_acceptance = coffee_coupons_df.groupby('weather')['Y'].agg(['count', 'mean']).round(3)
weather_acceptance.columns = ['Total Coupons', 'Acceptance Rate']
print("\nAcceptance by Weather:")
print(weather_acceptance)

# 4. Acceptance by age group
age_acceptance = coffee_coupons_df.groupby('age')['Y'].agg(['count', 'mean']).round(3)
age_acceptance.columns = ['Total Coupons', 'Acceptance Rate']
print("\nAcceptance by Age Group:")
print(age_acceptance)

# Create visualizations
plt.figure(figsize=(15, 10))

# 1. Visit Frequency Plot
plt.subplot(2, 2, 1)
sns.barplot(data=coffee_coupons_df, x='visit_frequency', y='Y')
plt.title('Acceptance by Visit Frequency')
plt.xlabel('Visit Frequency')
plt.ylabel('Acceptance Rate')
for i in plt.gca().patches:
    plt.gca().annotate(f'{i.get_height():.2%}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

# 2. Time of Day Plot
plt.subplot(2, 2, 2)
sns.barplot(data=coffee_coupons_df, x='time', y='Y')
plt.title('Acceptance by Time of Day')
plt.xlabel('Time')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation=45)
for i in plt.gca().patches:
    plt.gca().annotate(f'{i.get_height():.2%}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

# 3. Weather Plot
plt.subplot(2, 2, 3)
sns.barplot(data=coffee_coupons_df, x='weather', y='Y')
plt.title('Acceptance by Weather')
plt.xlabel('Weather')
plt.ylabel('Acceptance Rate')
for i in plt.gca().patches:
    plt.gca().annotate(f'{i.get_height():.2%}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

# 4. Age Group Plot
plt.subplot(2, 2, 4)
sns.barplot(data=coffee_coupons_df, x='age', y='Y')
plt.title('Acceptance by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation=45)
for i in plt.gca().patches:
    plt.gca().annotate(f'{i.get_height():.2%}', 
                      (i.get_x() + i.get_width()/2, i.get_height()),
                      ha='center', va='bottom')

plt.tight_layout()
plt.savefig('coffee_house_analysis.png')
plt.close() 