import requests

url = "https://instagram73.p.rapidapi.com/api/"

querystring = {"username":"m0nxt3r"}

headers = {
	"X-RapidAPI-Key": "2bc1dbb18fmsh6338ecc923b924bp1b71a2jsn643bb605ff8f",
	"X-RapidAPI-Host": "instagram73.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)