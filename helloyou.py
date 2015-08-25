#!/usr/bin/env python
from bottle import route, run, template, TEMPLATE_PATH, get, post, request
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
		conn.close()

TEMPLATE_PATH.insert(0,'/apps/helloyou/templates/')

@get('/')
def index():
	return template('index')

@post('/hello')
def hello():
	name = request.forms.get('name')
	if name:
		db = dbc()
		db.insert('insert into guests (name) values ("%s")' % name)
		return template('<b>Hello {{name}}</b>!<p><hr><br><a href="/">Back</a><br><a href="/list">List entries</a><p>', name=name)
	else:
		return template('index')

@route('/list')
def list():
	db = dbc()
	result = db.select('select * from guests order by entered')
	return template('list', result=result)

run(host='0.0.0.0', port=8080, debug=True, server='tornado')
