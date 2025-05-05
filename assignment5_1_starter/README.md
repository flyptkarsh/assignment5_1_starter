# Coupon Acceptance Analysis

## Project Overview
This project analyzes factors that influence whether drivers accept or reject coupons while driving. The analysis focuses on understanding the characteristics and behaviors of drivers who accept coupons versus those who don't.

## Key Findings

### Overall Acceptance Rate
- 57.41% of all coupons were accepted
- This indicates a generally positive response to coupon offers

### Bar Coupon Analysis
- **Visit Frequency Impact**
  - Regular bar visitors (>3 times/month): 76.9% acceptance rate
  - Infrequent visitors (≤3 times/month): 37.1% acceptance rate
  - This suggests that past behavior is a strong predictor of coupon acceptance

### Coffee House Coupon Analysis
- **Time of Day Impact**
  - Morning (10AM): 64.1% acceptance
  - Afternoon (2PM): 54.8% acceptance
  - Evening (6PM): 41.3% acceptance
- **Age Demographics**
  - Under 21: 69.7% acceptance
  - 50+: 42.0% acceptance
- **Weather Impact**
  - Rainy: 52.2% acceptance
  - Sunny: 50.4% acceptance
  - Snowy: 43.2% acceptance

## Recommendations

### For Bar Coupons
1. Target regular bar visitors for highest acceptance rates
2. Focus on customers who have demonstrated bar-going behavior
3. Consider time of day and weather conditions when distributing coupons

### For Coffee House Coupons
1. Target younger demographics, especially those under 21
2. Distribute coupons during morning and afternoon hours
3. Focus on regular coffee house visitors
4. Consider weather conditions, with higher acceptance during rainy and sunny conditions

## Technical Details
- Dataset: UCI Machine Learning Repository
- Sample Size: 12,684 observations
- Analysis Tools: Python, Pandas, Matplotlib, Seaborn
- Key Variables: Coupon type, time of day, weather, age, visit frequency

## Repository Contents
- `prompt.ipynb`: Main analysis notebook
- `coupon_visualization.py`: Code for coupon distribution visualization
- `temperature_visualization.py`: Code for temperature distribution analysis
- `bar_coupon_analysis.py`: Code for bar coupon analysis
- `coffee_house_analysis.py`: Code for coffee house coupon analysis
- `data/coupons.csv`: Original dataset
- Various visualization outputs (.png files) 