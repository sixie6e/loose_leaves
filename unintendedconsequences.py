import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Species': ['Buzzard', 'Buzzard', 'Red Kite', 'Red Kite'],
    'Time_Period': ['2005-2010', '2020-2022', '2005-2010', '2020-2022'],
    'Percent_High_Level_Positive': [2, 24, 15, 66]
}

df = pd.DataFrame(data)
fig, ax = plt.subplots(figsize=(10, 6))

species = df['Species'].unique()
time_periods = df['Time_Period'].unique()
x = np.arange(len(species)) 
width = 0.35 
rects1 = ax.bar(x - width/2, df[df['Time_Period'] == time_periods[0]]['Percent_High_Level_Positive'], width, label=time_periods[0], color='#4C72B0')
rects2 = ax.bar(x + width/2, df[df['Time_Period'] == time_periods[1]]['Percent_High_Level_Positive'], width, label=time_periods[1], color='#DD8452')

ax.set_ylabel('Percentage of Raptors with Very High SGAR Levels (>0.3 mg/kg)', fontsize=12)
ax.set_title('Increase in Severe Secondary Poisoning of UK Raptors (2005-2022)', fontsize=14, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(species, rotation=0, fontsize=12)
ax.legend(title='Time Period', fontsize=10)
ax.set_ylim(0, 100) # percentgae max

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

autolabel(rects1)
autolabel(rects2)

ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('secondarypoisoning.png')
plt.show()

print(df.to_csv('raptor_data.csv', index=False))
