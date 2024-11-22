#Варіант 3, завдання №2
import pandas as pd
import json
agrofirms = {"Agrorythm": 344,"West Bug": 832,"Green Pole": 216,"Lanna-agro": 932}
with open('agrofirms.json', 'w') as json_file:
    json.dump(agrofirms, json_file, indent=4)
print("Файл 'agrofirms.json' створено.")
areas = pd.Series(agrofirms)  
manarea = areas.mean() 
variations = areas - manarea  
print("Середнє арифметичне площі сільськогосподарських угідь:", manarea)
print("Відхилення від середнього арифметичного:")
print(variations)