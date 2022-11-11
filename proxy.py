import requests 
 
proxies = {'http': 'http://209.146.105.241:80'} 
response = requests.get('http://httpbin.org/ip', proxies=proxies) 
print(response.json()['origin']) # 190.64.18.162
