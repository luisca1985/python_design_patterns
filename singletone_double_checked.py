# Double Checked Locking singleton pattern


import threading

class SingletonDoubleChecked(object):

	# resources shared by each and every
	# instance

	__singleton_lock = threading.Lock()
	__singleton_instance = None

	# define the classmethod
	@classmethod
	def instance(cls):

		# check for the singleton instance
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()

		# return the singleton instance
		return cls.__singleton_instance

# main method
if __name__ == '__main__':

	# create class X
	class X(SingletonDoubleChecked):
		pass

	# create class Y
	class Y(SingletonDoubleChecked):
		pass

	A1, A2 = X.instance(), X.instance()
	B1, B2 = Y.instance(), Y.instance()

	assert A1 is not B1
	assert A1 is A2
	assert B1 is B2

	print('A1 : ', A1)
	print('A2 : ', A2)
	print('B1 : ', B1)
	print('B2 : ', B2)
