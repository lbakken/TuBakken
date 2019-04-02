import requests

adress = 'http://api.openweathermap.org/data/2.5/weather?appid=8b13ac7355b77d79be8fc42f5089313d&q='
city = input('What city?:\n')
url = adress + city
data = requests.get(url).json()

rn_kelvin = float(data['main']['temp'])
f_rn = ((rn_kelvin - 273.67)*(9/5))+32

high_kelvin = float(data['main']['temp_max'])
f_high = ((high_kelvin - 273.67)*(9/5))+32

low_kelvin = float(data['main']['temp_min'])
f_low = ((low_kelvin - 273.67)*(9/5))+32

print('Today in:', city, '\navg:', round(f_rn), '\nhigh:', round(f_high), '\nlow:', round(f_low))