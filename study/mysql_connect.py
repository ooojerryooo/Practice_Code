# Auther nmap
# coding=utf-8


import pymysql
conn = pymysql.connect(host="192.168.200.61",port=3306,user="root",passwd="root",db="test",charset="utf8")
cur = conn.cursor()
sql='select * from user'
values=cur.execute(sql)
print(values)
cur.close()
conn.close()