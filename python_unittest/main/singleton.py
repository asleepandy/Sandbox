

class Singleton(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


class Borg(object):
	_shared_state = {}

	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj


class Child(Borg):
	pass


class Demo(object):
	__x = 0

	def __init__(self, i):
		self.__i = i
		Demo.__x += 1

	def __str__(self):
		return str(self.__i)

	def hello(self):
		print("hello " + self.__str__())

	@classmethod
	def getX(cls):
		return cls.__x


class SubDemo(Demo):
	def __init__(self, i, j):
		super(SubDemo, self).__init__(i)
		self.__j = j

	def __str__(self):
		return super(SubDemo, self).__str__() + "+" + str(self.__j)


a = SubDemo(12, 34)
a.hello()
print("a.__x =", a.getX())
b = SubDemo(56, 78)
b.hello()
print("b.__x =", b.getX())
print()
print("a.__x =", a.getX())
print("b.__x =", b.getX())
