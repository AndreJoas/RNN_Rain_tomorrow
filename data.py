import requests

url = 'https://raw.githubusercontent.com/alan-barzilay/NLPortugues/master/Semana%2002/data/weatherAUS.csv'
response = requests.get(url)

with open('data/weatherAUS.csv', 'wb') as file:
    file.write(response.content)

