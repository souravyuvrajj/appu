import json
import requests
import os
import sys

_ROOT = os.path.expanduser('~')

if not os.path.exists(os.path.join(_ROOT, ".appu/")):
	os.makedirs(os.path.join(_ROOT, ".appu/"))

def configure():
	try:
		configuration_file = open(os.path.join(_ROOT, ".appu/config.json"), "w")
		api_key = input("What is your api_key?[6d60209987f0dbf1d9f94288b02f23ba]") or '6d60209987f0dbf1d9f94288b02f23ba'
		budget = input("What is your budget(per person/in your currency)?[100]") or 100
		try:
			budget = float(budget)
		except:
			budget = 100
			print ("Couldn't parse number. Going with default!")
		lat = input("What is your latitude?[26.1445]") or '26.1445'
		lon = input("What is your longitude?[91.7362]") or '91.7362'
		url = "https://developers.zomato.com/api/v2.1/cities?lat=%s&lon=%s" %(lat, lon)
		city_id = False
		headers = {'Accept' : 'application/json', 'user_key': api_key, 'User-Agent': 'curl/7.35.0'}
		try:
			response = requests.get(url, headers = headers)
			if response.status_code == 200:
				data = response.json()
				if data['status'] == 'success':
					city_id = data['location_suggestions'][0]['id']
			elif response.status_code == 403:
				print ('Invalid API Key')
		except:
			print ('Something went wrong while parsing the city!')
			sys.exit()
		if city_id:
			configuration = {"budget" : budget, "lat": lat, "lon": lon, "api_key": api_key, 'city_id': city_id}
			configuration_file.write(json.dumps(configuration))
		else:
			print ('Your city isnt supported')
			sys.exit()
	except:
		print ("Something went wrong! Try Again?")
		sys.exit()

try:
	config = json.loads(open(os.path.join(_ROOT, ".appu/config.json"), "r").read())
except:
	print ("no config file found")
	configure()
	config = json.loads(open(os.path.join(_ROOT, ".appu/config.json"), "r").read())
