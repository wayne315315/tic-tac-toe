import time


__all__ = ['timefn']


def timefn(func):

	def new_func(*args, **kwargs):
		t1 = time.time()
		func(*args, **kwargs)
		t2= time.time()
		print("%s took %f seconds"%(func.__name__, t2-t1))

	return new_func

