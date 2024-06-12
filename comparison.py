import pandas as pd
import matplotlib.pyplot as plt

# Load the data
brown_data = pd.read_csv("brown.csv")
jokic_data = pd.read_csv("jokic.csv")

# Calculate points per game for each player
brown_data['PPG'] = brown_data['PTS'] / brown_data['G']
jokic_data['PPG'] = jokic_data['PTS'] / jokic_data['G']

# Calculate assists per game for each player
brown_data['APG'] = brown_data['AST'] / brown_data['G']
jokic_data['APG'] = jokic_data['AST'] / jokic_data['G']

# Calculate rebounds per game for each player
brown_data['RPG'] = brown_data['TRB'] / brown_data['G']
jokic_data['RPG'] = jokic_data['TRB'] / jokic_data['G']

# Calculate field goal percentage for each player
brown_data['FG%'] = (brown_data['FG'] / brown_data['FGA']) * 100
jokic_data['FG%'] = (jokic_data['FG'] / jokic_data['FGA']) * 100

# Calculate three-point percentage for each player
brown_data['3P%'] = (brown_data['3P'] / brown_data['3PA']) * 100
jokic_data['3P%'] = (jokic_data['3P'] / jokic_data['3PA']) * 100

# Calculate free throw percentage for each player
brown_data['FT%'] = (brown_data['FT'] / brown_data['FTA']) * 100
jokic_data['FT%'] = (jokic_data['FT'] / jokic_data['FTA']) * 100

# Create a dataframe for comparison
comparison_data = pd.DataFrame({
    'Player': ['Jaylen Brown', 'Nikola Jokic'],
    'PPG': [brown_data['PPG'].mean(), jokic_data['PPG'].mean()],
    'APG': [brown_data['APG'].mean(), jokic_data['APG'].mean()],
    'RPG': [brown_data['RPG'].mean(), jokic_data['RPG'].mean()],
    'FG%': [brown_data['FG%'].mean(), jokic_data['FG%'].mean()],
    '3P%': [brown_data['3P%'].mean(), jokic_data['3P%'].mean()],
    'FT%': [brown_data['FT%'].mean(), jokic_data['FT%'].mean()]
})

# Plot comparison
comparison_data.plot(x='Player', kind='bar', figsize=(12, 8))
plt.title('Playoff Performance Comparison: Jaylen Brown vs Nikola Jokic')
plt.xlabel('Player')
plt.ylabel('Average')
plt.xticks(rotation=0)
plt.legend(["PPG", "APG", "RPG", "FG%", "3P%", "FT%"])
plt.show()
