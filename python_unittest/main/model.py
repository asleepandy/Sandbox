# -*- coding: utf-8 -*-
'''
Data Model : collections
Note : This is collections used by Payment Center
Author : Neo
'''

from mongoengine import *
from datetime import datetime
from mongoengine.fields import DateTimeField

'''
2015-04-02 Neo
Collection-package 付費方案
2015-05-13 Andy
add field "appKey", "payType"
'''
class package(Document):
	pkId = StringField()
	appKey = StringField()
	pkName = StringField()
	payType = StringField()
	price = IntField()
	imgUrl = StringField()
	days = IntField()

	meta = {
		'collection': 'package',
	}

	def toDict(self):
		return {
			'pkId': self.pkId,
			'appKey': self.appKey,
			'pkName': self.pkName,
			'payType': self.payType,
			'price': self.price,
			'imgUrl': self.imgUrl,
			'days': self.days
		}

'''
2015-04-02 Neo
Collection-appCode APP的Key
2015-05-15 Andy
add field "code"
'''
class appCode(Document):
	appName = StringField()
	key = StringField()
	code = StringField()

	meta = {
		'collection': 'appCode',
#		'indexes': ['email']
	}

	def toDict(self):
		return {
			'appName': self.appName,
			'key': self.key,
			'code': self.code
		}

	#lastModTime = DateTimeField()
	#lastModUser = GenericReferenceField()
	#deleted = BooleanField(default=False)

'''
2015-04-02 Neo
Collection-apiAccLog API的讀取記錄
'''
class apiAccLog(Document):
	appKey = StringField()
	apiName = StringField()
	accTime = DateTimeField()

	meta = {
		'collection': 'apiAccLog',
	}

	def toDict(self):
		return {
			'appKey': self.appKey,
			'apiName': self.apiName,
			'accTime': self.accTime
		}

'''
2015-04-02 Neo
Collection-sysLog 系統記錄
'''
class sysLog(Document):
	apiName = StringField()
	message = StringField()
	createTime = DateTimeField()

	meta = {
		'collection': 'sysLog',
	}

	def toDict(self):
		return {
			'apiName': self.apiName,
			'message': self.message,
			'createTime': self.createTime
		}


class paymentInfo(Document):
	'''
	2015-05-13 Andy
	Collection-paymentInfo 會員支付記錄資料
	'''
	paymentId = StringField(required=True)
	#身分編號 會員：user_id 訪客：token
	rankId = StringField()
	memberId = IntField(required=True)

	#TODO:這三個欄位要討論是不是要記
	device = StringField(required=True)
	ver = StringField()
	userKey = StringField()

	appKey = StringField(required=True)
	pkId = StringField()
	#支付方式
	payType = StringField(required=True)
	orderTime = DateTimeField(required=True)
	payAmount = IntField()
	payTime = DateTimeField(default = None)
	lastModTime = DateTimeField(required=True)
	showRecord = BooleanField(default = True)
	status = IntField(required=True, default = 0)
	guestTransId = StringField()

	meta = {
		'collection': 'paymentInfo',
	}

	@staticmethod
	def genPaymentId(_code, _type, _amount):
		'''
		産生訂單編號,格式如下
		産品別 支付方式 年 月 日 檢查碼 百分之1秒
		K     13     15 05 18 6    3772046  ?
		檢查碼產生原理:
		3772046 , 訂單金額1000
		(3*1+ 7*2+ 7*3+ 2*4+ 0*5+ 4*6+ 6*7)＝112
		(1*4+ 0*3+ 0*2+ 0*1) = 4 ,若交易金額為15,000,則最高位乘數為5,以此類推
		112+4 = 116 , 取最後一碼,所以檢核碼是7
		@param _code: 産品代碼appCode.code
		@param _type: 支付方式package.payType
		@param _amount: 本次訂單交易金額 
		'''
		d = datetime.now()
		t = d.time()

		s = _code + str(_type) + d.strftime('%y%m%d')
		t = '{:0>7d}'.format((t.hour*3600 + t.minute*60 + t.second)*100 + t.microsecond/10000)
		c = 0

		''' 産生檢查碼 '''
		for idx in range(0, len(t)):
			c += (int(t[idx]) * (idx+1))

		a = str(_amount)
		l = len(a)
		for idx in range(0, l):
			c += (int(a[idx]) * (l-idx))

		c = str(c)
		c = c[len(c)-1]
		return s + c + t

	def toDict(self):
		return {
			'paymentId': self.paymentId,
			'rankId': self.rankId,
			'memberId': self.memberId,
			'device': self.device,
			'ver': self.ver,
			'userKey': self.userKey,
			'appKey':self.appKey,
			'pkId':self.pkId,
			'payType':self.payType,
			'orderTime':self.orderTime,
			'payAmount':self.payAmount,
			'payTime':self.payTime,
			'lastModTime':self.lastModTime,
			'showRecord':self.showRecord,
			'status': self.status,
			'guestTransId': self.guestTransId
		}

class product(EmbeddedDocument):
	id = StringField()
	name = StringField()
	price = IntField()
	qty = IntField()

class paymentDetail(Document):
	paymentId = StringField()
	detailStr = StringField()
	detail = ListField(EmbeddedDocumentField(product))
	lastModTime = DateTimeField()

	meta = {
		'collection': 'paymentDetail'
	}

	def toDict(self):
		return self.to_json()

class monthlyPaymentProfile(Document):
	'''
	2015-07-02 Andy
	Collection-monthlyPaymentProfile 月租連續扣款屬性資料
	'''
	profileId = StringField(required=True)
	lastModTime = DateTimeField()
	appKey = StringField(required=True)
	payType = StringField(required=True)
	transType = StringField(required=True)
	directDebit = IntField(required=True, default=1)
	startDebitDate = DateTimeField()
	stopDebitDate = DateTimeField()
	lastDebitDate = DateTimeField()

	meta = {
		'collection': 'monthlyPaymentProfile',
	}

	def toDict(self):
		return {
			'profileId': self.profileId,
			'lastModTime': self.lastModTime,
			'appKey': self.appKey,
			'payType': self.payType,
			'transType': self.transType,
			'directDebit': self.directDebit,
			'startDebitDate': self.startDebitDate,
			'stopDebitDate': self.stopDebitDate,
			'lastDebitDate': self.lastDebitDate
		}

class paymentAccess(Document):
	'''
	2015-05-13 Andy
	Collection-paymentAccess 訂單執行MySQL指令記錄資料
	'''
	paymentId = StringField(required=True)
	uId = StringField(required=True)
	pkId = StringField(required=True)
	before = StringField(required=True)
	updateString = StringField(required=True)
	status = StringField(required=True)
	accTime = DateTimeField()
	lastModTime = DateTimeField()

	meta = {
		'collection': 'paymentAccess',
	}

	def toDict(self):
		return {
			'paymentId': self.paymentId,
			'uId': self.uId,
			'pkId': self.pkId,
			'before': self.before,
			'updateString': self.updateString,
			'status': self.status,
			'accTime': self.accTime,
			'lastModTime': self.lastModTime
		}


class transMyCard(Document):
	'''
	2015-05-13 Andy
	Collection-transMyCard MyCard交易記錄資料
	'''
	paymentId = StringField(required=True)
	status = IntField(required=True, default=1)
	transType = StringField(required=True)
	authCode = StringField()
	tradeType = IntField()
	cardId = StringField()
	cardPwd = StringField()
	cardKind = IntField()
	cardPoint = IntField()
	saveSeq = StringField()
	oProjNo = StringField()
	lastModTime = DateTimeField()
	ReturnMsgNo = StringField()
	ReturnMsg = StringField()
	ErrorMsgNo = StringField()
	ErrorMsg = StringField()

	meta = {
		'collection': 'transMyCard'
	}
	def toDict(self):
		return {
			'paymentId': self.paymentId,
			'status': self.status,
			'transType': self.transType,
			'authCode': self.authCode,
			'tradeType': self.tradeType,
			'cardId': self.cardId,
			'cardPwd': self.cardPwd,
			'cardKind': self.cardKind,
			'cardPoint': self.cardPoint,
			'saveSeq': self.saveSeq,
			'oProjNo': self.oProjNo,
			'lastModTime': self.lastModTime,
			'ReturnMsgNo': self.ReturnMsgNo,
			'ReturnMsg': self.ReturnMsg,
			'ErrorMsgNo': self.ErrorMsgNo,
			'ErrorMsg': self.ErrorMsg
		}
