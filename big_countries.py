import pandas as pd

# Предполагается, что DataFrame world уже создан

big_countries = world[(world['area'] > 3000000) | (world['population'] > 25000000)]
print(big_countries[['name', 'continent', 'area', 'population']])