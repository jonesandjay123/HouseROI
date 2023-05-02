import requests
from tool.helper import Helper 



API_KEY = Helper.read_access_token('access_token.txt')
city = "Newark"
url = f"https://api.bridgedataoutput.com/api/v2/zgecon/region?access_token={API_KEY}&regionCity={city}"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)