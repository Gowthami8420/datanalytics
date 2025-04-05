import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s- %(levelname)s-%(message)s')
#the level is set to warning by default
#if you want info or debug logs you have to set the level lower

logging.debug('Hello,Debug!')
logging.info('Hello,Info!')
logging.warning('Hello,warning!')
logging.error('Hello,Error!')
logging.critical('Hello,critical!')