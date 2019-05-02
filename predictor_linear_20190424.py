from sklearn.externals import joblib
import numpy as np

model = joblib.load('./models/linear-regression_20190430.joblib')

# Processing the new case to estimate:
print('\n\nFor Difficulty Reference: \n x = hours to finish each page\n' +
    'Level 1: x < 0.5 \n' +
        'Level 2: 0.5 <= x < 1.25\n' +
            'Level 3: 1.25 <= x < 2.5\n' +
                'Level 4: 2.5 <= x <3.75\n' +
                    'Level 5: x >= 3.75')

# Ask for inputs about the project
pages = int(input('Number of pages: '))

modeling = input('3D modeling required (yes or no)?: ')

level = int(input('Difficulty (1-5): '))


#process modeling input
if modeling == 'yes':
    modeling = 1
elif modeling == 'no':
    modeling = 0
else:
    print('error')
    pass

# plug user inputs into the model and store the prediction
estimate = model.predict([[pages, modeling, level]])

model_output = estimate[0]
# multiplier to give myself some wiggle room
wiggle = 1.15
final_estimate = model_output * wiggle

print('The final estimate is: {}'.format(
        np.around(final_estimate, decimals=1)
    ))