import requests

_url1 = 'https://api.ipfind.com?ip='
address = input('What is the IP?:\n')
key = '&auth=a864df2c-e745-4463-affb-6f8c78e7953f'
url = _url1 + address + key
data = requests.get(url).json()
cooldata = data['continent']
coolerdata = data['country']
coolestdata = data['city']
lat = data['latitude']
long = data['longitude']

print('IP is located:\n',cooldata,'\n',coolerdata,'\n',coolestdata,'\n',lat,'\n',long)