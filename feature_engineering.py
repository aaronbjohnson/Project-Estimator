import pandas as pd
from utilities import remove_column
import os
import sys

'''
This will separate difficulty into 5 levels according to a more intuitive
hour / page estimation.
'''

# Project's root directory
PROJ_ROOT = os.getcwd()

# Destination for processed data
engineered_dir = str(PROJ_ROOT + './data/engineered_data.csv')

# Import processed data
df = pd.read_csv('./data/processed_20190430_projects.csv')

# Feature Engineering

# Create a new variable that records 'hours' / 'number_pages'
df['hour_page'] = df['hours'] / df['number_pages']

# ALTERNATE USING MIN AND MAX
hp_min = df.hour_page.min()
hp_max = df.hour_page.max()
hp_std = df.hour_page.std()
hp_range = hp_max - hp_min
# as of 20190213: introducing 5 levels instead of 4
hp_bin = hp_range / 5

# Create variables to store location of difficulty bins
# Use this if we're NOT including the visio record
level_one = hp_min + hp_bin
level_two = level_one + hp_bin
level_three = level_two + hp_bin
level_four = level_three + hp_bin

def get_difficulty(row):
    difficulty = 0
    if row.hour_page < level_one:
        difficulty = 1
    elif (row.hour_page >= level_one) & (row.hour_page < level_two):
        difficulty = 2
    elif (row.hour_page >= level_two) & (row.hour_page < level_three):
        difficulty = 3
    elif (row.hour_page >= level_three) & (row.hour_page < level_four):
        difficulty = 4
    elif (row.hour_page >= level_four):
        difficulty = 5
    else:
        return difficulty

    return difficulty

# Create Difficulty column
df['difficulty'] = df.apply(get_difficulty, axis=1)

'''
Choosing not to remove the 'hour_page' here as we want to graph it in EDA
'''
# Remove 'hour_page'
#remove_column(df, 'hour_page')

# Save the new dataset to csv
print('Storing Processed Data...')
df.to_csv(engineered_dir, index=False)
print('Processed csv file has been saved.')

# Print guide for difficulty variable
print('Difficulty Guide: \n')
print('X = hour per page')
print('\nLevel 1: X < ' + str(level_one))
print('\nLevel 2: ' + str(level_one) + ' <= X > ' + str(level_two))
print('\nLevel 3: ' + str(level_two) + ' <= X > ' + str(level_three))
print('\nLevel 4: ' + str(level_three) + ' <= X > ' + str(level_four))
print('\nLevel 5: ' + str(level_four) + ' <= X')
