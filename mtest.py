# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime
###############################################################################
#                       股票機器人 Python基礎教學 【pymongo教學】                      #
###############################################################################

# Authentication Database認證資料庫
Authdb='linechatbot'

client = MongoClient('mongodb+srv://eason880913:EASON880913@cluster0.8gor1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
db = client[Authdb]


collect = db['table_a1']
collect.insert_one({"stock": 'tock',
                    "data": 'care_stock',
                    "bs": 'bs',
                    "price": 'price',
                    "date_info": datetime.datetime.utcnow()
                    })