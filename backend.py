import requests
api_key = 'xxxxxxxxxxxxxxxxxxx'



def get_data(place, days=None, type_=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    content = response.json()
    return content



if __name__== '__main__':
    print(get_data(place='tokyo'))

