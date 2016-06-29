import httplib, urllib
import hashlib

HOST = 'facebook.com'
account, password = '', ''
class Facebook_Info(account, password):
	def FBook_connection(self):
		global account = account
		global password = password
		conn = httplib.HTTPConnection(HOST, 80)
		