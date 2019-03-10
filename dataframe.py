dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
list = pd.DataFrame(dict)
'''using DataFrame from pandas'''
print(list)
list.index = ["BR","RU","IN","CH","SA"]
print(list)
'''name the index by object.index'''
insurance = pd.read_csv('FL_insurance_sample.csv')
'''using panda.read_csv to visualize a csv file'''
print(insurance)

insurance = pd.read_csv('FL_insurance_sample.csv',index_col=0)

print(list['country'])
'''single bracket with output a Panda Series, one dimension object'''

print(list[['country']])
'''double bracket with putput a Panda dataframe, 2 dimension object, many  column with dif types'''

dates = pd.date_range('20190303',periods = 10)
print(dates)

print(list[['country','area']])
insurance = pd.read_csv('FL_insurance_sample.csv', index_col=0)
print(insurance[0:10])
