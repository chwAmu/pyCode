import logging
import loggingAdv2
# now the logging is shareing the same logger
# so if you config your logger here, and then import the other modules
# that with logging, the config will be overwritten.
# but after we re-create a new logger for module loggingAdv2
# it will be work!

# create a logger variables
logger=logging.getLogger(__name__)	
# set the level
logger.setLevel(logging.DEBUG)
# set the format
formatter=logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
# set the FileHandler
file_handler=logging.FileHandler('Sample.log')
# set the format
file_handler.setFormatter(formatter)
# set the level
file_handler.setLevel(logging.ERROR)
# add the handler
logger.addHandler(file_handler)
# output to console
stream_handler=logging.StreamHandler()
# format
stream_handler.setFormatter(formatter)
# add handler
logger.addHandler(stream_handler)

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mult(x,y):
	return x*y

def div(x,y):
	try:
		result=x/y
	except ZeroDivisionError:
		# logger.error('div by zero')
		logger.exception('div by zero')
	else:
		return result

x=5
y=0

a=add(x,y)
b=div(x,y)
logger.debug('add : {} + {} = {} '.format(x,y,a))
