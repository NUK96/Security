#coding:utf-8

from urllib import request
import ssl

url = 'https://api.ipplus360.com/ip/geo/v1/street/'

response = request.urlopen(url,timeout=5,)
page = response.read().decode("utf-8")
print(page)