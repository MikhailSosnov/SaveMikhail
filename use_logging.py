import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'),'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.log')

print('Save log in ', logging_file)

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = logging_file, filemode ='w')

logging.debug('Begin program')
logging.info('Somthing action')
logging.warning('Program is dying')

