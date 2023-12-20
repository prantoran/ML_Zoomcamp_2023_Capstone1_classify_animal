import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# url = 'https://g4ep6p5nkd.execute-api.eu-west-1.amazonaws.com/test/predict'
url = 'https://7sd6z109se.execute-api.eu-west-1.amazonaws.com/test/predict'

data = {'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS43GnsWMaclquIceMZNGL6uUVeeHmAkh3lphE5M3Wh8A&s'}

result = requests.post(url, json=data).json()
print(result)