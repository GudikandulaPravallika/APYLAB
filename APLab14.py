import pandas as pd
import numpy as np
exam_data  = {'name': ['Gopal', 'Keshav', 'Radha', 'Mohan', 'Gokul', 'Krish', 'Achyuta', 'Kanha', 'Damodhar', 'Vasudev'],
        'score': [12.5, 9, 15.5, np.nan, 9, 20, 15, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(2, 15)])
