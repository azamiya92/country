#/usr/bin/env python

import requests
import sys
import os

#workon country
sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

#import Country

from main.models import Country

response = requests.get('http://restcountries.eu/rest/v1/all')

print response

response_dict = response.json()

#print response_dict

for data in response_dict:
	#print data['name']
	print '-----------'
	country,created = Country.objects.get_or_create(name=data['name'])
	print created
	country.capital = data['capital']
	country.population = data['population']
	country.save()



