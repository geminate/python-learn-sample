import requests
import time
from pyquery import PyQuery as pq

import pymysql.cursors


def initMysql():
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='pylearn',
        charset='utf8'
    )
    return connect


def getByAid(aid, connect):
    try:
        r = requests.get('http://api.douban.com/v2/movie/subject/' + str(aid), timeout=6).json()
        print(r)
    except Exception as e:
        print(str(aid) + ":  " + str(e))


start = 1764790
end = 27000000

connect = initMysql()

for aid in range(start, end):
    getByAid(aid, connect)
