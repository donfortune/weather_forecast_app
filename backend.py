import requests
api_key = '174db087491c0816ee287b06e80c2f97'




def get_data(place, days=None, type_=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if type_ == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if type_ == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data




if __name__== '__main__':
    print(get_data(place='tokyo', days=3, type_='Sky'))

