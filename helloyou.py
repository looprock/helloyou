#!/usr/bin/env python
from bottle import route, run, template, TEMPLATE_PATH, get, post
import MySQLdb

class dbc(object):
	def __init__(self):
		self.db_host = "10.0.2.15"
		self.db_username = "guestbook"
		self.db_password = "guestbook"
		self.db_name = "guestbook"
	def insert(self, statement):
		conn = MySQLdb.Connection(host=self.db_host, user=self.db_username, passwd=self.db_password, db=self.db_name)
		curs = conn.cursor()
		curs.execute(statement)
		conn.commit()
		conn.close()
	def select(self, statement):
		conn = MySQLdb.Connection(host=self.db_host, user=self.db_username, passwd=self.db_password, db=self.db_name)
		curs = conn.cursor()
		curs.execute(statement)
		conn.commit()
		result = curs.fetchall()
		return result
	def close(self):
		conn.close()

TEMPLATE_PATH.insert(0,'/apps/helloyou/templates/')

@get('/')
def index():
	return template('index')

@post('/hello')
def hello(name):
	name = request.forms.get('name')
	if name:
		return template('<b>Hello {{name}}</b>!', name=name)
	else:
		return template('index')

run(host='0.0.0.0', port=8080, debug=True, server='tornado')
