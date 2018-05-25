import logging

# create a logger variables
logger=logging.getLogger(__name__)	
# 
logger.setLevel(logging.INFO)
# 
formatter=logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
# 
file_handler=logging.FileHandler('loggingAdv2.log')
# 
file_handler.setFormatter(formatter)
# 
logger.addHandler(file_handler)


class Motor:

	def __init__(self,voltage,current):
		self.voltage=voltage
		self.current=current
		logger.info('Motor profile is created with :{}V and {}A'.format(self.voltage,self.current))

	@property
	def getPower(self):
		return '{} * {} = {}'.format(self.current,self.voltage,self.current*self.voltage)

	@property
	def getDat(self):
		return 'v={},a={}'.format(self.voltage,self.current)


print('run..')
m1=Motor(380,2)
m2=Motor(220,1.4)
	
	