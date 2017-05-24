#!/usr/bin/env python
#coding:utf-8

import sys
import os
from subprocess import PIPE, Popen

class Process(object):
	'''memcached rc script'''
	args = {
		'USER':'memcached',
		'PORT':11211,
		'MAXCONN':1024,
		'CACHESIZE':64,
		'OPTIONS':''}

	def __init__(self, name, program, workdir):
		self.name = name
		self.program = program
		self.workdir = workdir

	def _init(self):
		'''/var/tmp/memcached'''
		if not os.path.exists(self.workdir):
			os.mkdir(self.workdir)
			os.chdir(self.workdir)
	
	def _pidFile(self):
		'''/var/tmp/memcache/memcached.pid'''
		return os.path.join(self.workdir, '%s.pid' %self.name)

	def _writePid(self):
		if self.pid:
			with open(self._pidFile(), 'w') as fd:
				fd.write(str(self.pid))
	def _readConf(self, f):
		with open(f) as fd:
			lines = fd.readlines()
			return dict([i.strip().replace('"', '').split('=') for i in lines])

	def _parseArgs(self):
		conf = self._readConf('/etc/sysconfig/memcached')
		if 'USER' in conf:
			self.args['USER'] = conf['USER']
		if 'PORT' in conf:
			self.args['PORT'] = conf['PORT']
		if 'MAXCONN' in conf:
			self.args['MAXCONN'] = conf['MAXCONN']
		if 'CACHESIZE' in conf:
			self.args['CACHESIZE'] = conf['CACHESIZE']
		options = ['-u', self.args['USER'],
			   '-p', self.args['PORT'],
			   '-m', self.args['CACHESIZE'],
			   '-c', self.args['MAXCONN']]
		return options	

	def start(self):
		self._init()
		cmd = [self.program] + self._parseArgs() + ['-d', '-P', self._pidFile()]
		print cmd
		p = Popen(cmd, stdout=PIPE)
#		self.pid = p.pid
#		self._writePid()
		print '%s start Sucessful' %self.name
	
	def _getPid(self):
		p = Popen(['pidof', self.name], stdout = PIPE)
		pid = p.stdout.read().strip()
		return pid

	def stop(self):
		pid = self._getPid()
		if pid:
			os.kill(int(pid), 15)
			if os.path.exists(self._pidFile()):
				os.remove(self._pidFile())
			print '%s is stopped' %self.name
			
	def restart(self):
		self.stop()
		self.start()

	def status(self):
		pid = self._getPid()
		if pid:
			print '%s is already running' %self.name
		else:
			print '%s is not running' %self.name
	def help(self):
		print 'Usage: %s {start|stop|restart|status} ' %__file__
def main():
	name = 'memcached'
	prog = '/usr/bin/memcached'
	wd = '/var/tmp/memcached'
	pm = Process(name = name, program = prog,  workdir = wd)
	try:
		cmd = sys.argv[1]
	except IndexError, e:
		print 'Option error'
		sys.exit()
	if cmd == 'start':
		pm.start()
	elif cmd == 'stop':
		pm.stop()
	elif cmd == 'restart':
		pm.stop()
		pm.start()
	elif cmd == 'status':
		pm.status()
	else:
		pm.help()

if __name__ == '__main__':
	main()
