import sqlite3

class singletonDB():
	_instance = None
	def __new__(self):
		if not self._instance:
			self._instance = super(singletonDB,self).__new__(self)
			self.database = sqlite3.connect('./database/users.db', check_same_thread=False)
		return self._instance


