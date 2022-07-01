import pandas as pd

results = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
print(results)

#Rename columns
results.rename(columns={'FTHG':'home_goals','HTR':'IDK'}, inplace=True)
print(results)