# -*- coding:utf-8 -*-
import urllib.request
from conx import station_names
from json import loads

city={}
for i in station_names.split('@'):
    if not i:#如果i不存在，contuen
        continue
    #print(i.split('|')[2])
    city[i.split('|')[1]]=i.split('|')[2]
#print(city)
train_date='2017-12-26'
from_station=city['长沙']
to_station=city['成都']



def getList():
    req=urllib.request.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
    html=req.read()
    #print(html)
    dict=loads(html)
    return dict['data']['result']

a=0
#[3]--车次
#[8]--出发时间
#[9]--到达时间
#[23]--软卧
#[17]--一等座
#[30]--二等座
for re in getList():
    # for i in re.split('|'):
    #     print('[%s]' %a,i)
    #     a += 1
    # a=0
    z=re.split('|')
    if z[30] == u'无' or not z[30]:
        continue
    print(u'有票','车次:%s,%s' %(z[3],z[30]))

