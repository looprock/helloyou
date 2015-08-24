#!/usr/bin/env python
from bottle import route, run, template
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

@get('/')
def index():
		return '''<form action="hello" method="post">
		Hi please enter your name for the guestbook!<p>
		<input name="name"     type="text" />
		<INPUT TYPE="submit" value="L">
		</form>'''

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=8080, debug=True, server='tornado')
