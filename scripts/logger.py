#!/usr/bin/env python
#coding:utf8

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logfile = '/tmp/logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)


ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')

