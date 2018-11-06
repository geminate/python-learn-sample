import requests
import time

import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='pylearn',
    charset='utf8'
)
cursor = connect.cursor()

# 起始 和 终止 AID
startAid = 1
endAid = 1000000

# 循环请求 B站 接口
for aid in range(startAid, endAid):
    payload = {'aid': aid}
    while True:
        try:
            r = requests.get('http://api.bilibili.com/archive_stat/stat', params=payload, timeout=6).json()
            print(r['code'])

            if r['code'] == 0:
                print(r['data'])

                # 数据库操作语句
                r = cursor.executemany('insert into `bilibili-data-archive` values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)',
                                       [(r['data']['aid'] if type(r['data']['aid']) == int else None,
                                         r['data']['view'] if type(r['data']['view']) == int else None,
                                         r['data']['danmaku'] if type(r['data']['danmaku']) == int else None,
                                         r['data']['reply'] if type(r['data']['reply']) == int else None,
                                         r['data']['favorite'] if type(r['data']['favorite']) == int else None,
                                         r['data']['coin'] if type(r['data']['coin']) == int else None,
                                         r['data']['share'] if type(r['data']['share']) == int else None,
                                         r['data']['now_rank'] if type(r['data']['now_rank']) == int else None,
                                         r['data']['his_rank'] if type(r['data']['his_rank']) == int else None,
                                         r['data']['like'] if type(r['data']['like']) == int else None,
                                         r['data']['dislike'] if type(r['data']['dislike']) == int else None,
                                         r['data']['no_reprint'] if type(r['data']['no_reprint']) == int else None,
                                         r['data']['copyright'] if type(r['data']['copyright']) == int else None
                                         )])
                # 提交语句
                connect.commit()
            break
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(3)
        except Exception as e:
            print(e)
            time.sleep(3)

cursor.close()
connect.close()
