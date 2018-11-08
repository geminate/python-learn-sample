import requests
from utils import initMysql, getByAid

r = requests.get('https://segmentfault.com/blogs/newest?page=' + str(1500), timeout=10)
print(r.text)
