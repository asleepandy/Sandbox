import pprint
from datetime import datetime

from mongoengine import *
from pymongo import MongoClient
from pymongo import ReadPreference

from model import apiAccLog

host = '10.1.3.134'
port = 27017
db = 'payment'
table = 'apiAccLog'


def connect_db_by_pymongo(host, port):
    pool = MongoClient(host, port)
    return pool[db]


def get_data_by_pymongo():
    db = connect_db_by_pymongo(host, port)
    r = db.get_collection(table).find({'accTime': {'$gte': datetime(2015, 5, 27), '$lt': datetime(2015, 5, 29)}}).limit(10)
    for _r in r:
        pprint.pprint(_r)

    # db.get_collection(table).insert_one({'appKey': 'ttest', 'apiName': 'gogoro', 'accTime': datetime.now()})
    # db.get_collection(table).delete_one({'appKey': 'ttest'})


get_data_by_pymongo()


def connect_db_by_mongoengine(host, port, db):
    connect(db, host=host, port=port, tz_aware=True, read_preference=ReadPreference.PRIMARY)


def get_data_by_mongoengine():
    connect_db_by_mongoengine(host, port, db)
    logs = apiAccLog.objects().limit(10)
    for l in logs:
        print l.toDict()

    apiAccLog(appKey='ttest', apiName='gogoro', accTime=datetime.now()).save()
    apiAccLog.objects(appKey='ttest').delete()

# get_data_by_mongoengine()
