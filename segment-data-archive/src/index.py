import requests
import time

r = requests.get('https://segmentfault.com/a/1190000016918813', timeout=6)

print(r.text)
