# import logging
#
# logging.basicConfig(filename='divive.log',
#                     filemode='w',
#                     format='%(name)s-%(levelname)s-%(message)s')
# logging.warning('this will get log to a file')

import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log',filemode='w', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()