# import os
# import django
# import pandas as pd
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
# django.setup()

# from ProjectApp.models import City

# data = pd.read_csv('cities.csv', encoding = "ISO-8859-1")

# cities = []
# for row in data.iloc[:]['ùí_éùåá_ìåòæé']:
#     cities.append(row)

# while ' ' in cities:
#     cities.remove(' ')

# for city in cities:
#     print(f'ADDING {city}')
#     City.objects.create(city = city)