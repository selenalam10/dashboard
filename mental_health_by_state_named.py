import pandas as pd

# Load the cleaned CSV instead of the large .XPT
df = pd.read_csv("cleaned_brfss.csv")

# Calculate depression % by state
depression_by_state = (
    df.groupby('_STATE')['ADDEPEV3']
    .apply(lambda x: (x == 1).mean() * 100)
    .round(2)
    .reset_index(name='Depression_Pct')
)

# Calculate average mentally unhealthy days by state
mental_days_by_state = (
    df.groupby('_STATE')['MENTHLTH']
    .mean()
    .round(2)
    .reset_index(name='Avg_Unhealthy_Days')
)

# Merge both
summary = pd.merge(depression_by_state, mental_days_by_state, on='_STATE')

# Map FIPS to state names
fips_to_state = {
    1: 'Alabama', 2: 'Alaska', 4: 'Arizona', 5: 'Arkansas', 6: 'California',
    8: 'Colorado', 9: 'Connecticut', 10: 'Delaware', 11: 'D.C.', 12: 'Florida',
    13: 'Georgia', 15: 'Hawaii', 16: 'Idaho', 17: 'Illinois', 18: 'Indiana',
    19: 'Iowa', 20: 'Kansas', 21: 'Kentucky', 22: 'Louisiana', 23: 'Maine',
    24: 'Maryland', 25: 'Massachusetts', 26: 'Michigan', 27: 'Minnesota',
    28: 'Mississippi', 29: 'Missouri', 30: 'Montana', 31: 'Nebraska',
    32: 'Nevada', 33: 'New Hampshire', 34: 'New Jersey', 35: 'New Mexico',
    36: 'New York', 37: 'North Carolina', 38: 'North Dakota', 39: 'Ohio',
    40: 'Oklahoma', 41: 'Oregon', 42: 'Pennsylvania', 44: 'Rhode Island',
    45: 'South Carolina', 46: 'South Dakota', 47: 'Tennessee', 48: 'Texas',
    49: 'Utah', 50: 'Vermont', 51: 'Virginia', 53: 'Washington',
    54: 'West Virginia', 55: 'Wisconsin', 56: 'Wyoming'
}

summary['State'] = summary['_STATE'].map(fips_to_state)
summary = summary[['State', 'Depression_Pct', 'Avg_Unhealthy_Days']]
summary = summary.sort_values('Depression_Pct', ascending=False)

# Print or save the summary
print(summary)
