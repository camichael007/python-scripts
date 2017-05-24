#!/usr/bin/env python
#coding:utf8
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-c', '--char',
				dest = 'chars',
				action = 'store_true',
				default = False,
				help = 'only count chars')
parser.add_option('-w', '--word',
				dest = 'words',
				action = 'store_true',
				default = False,
				help = 'only count words')
parser.add_option('-l', '--line',
				dest = 'lines',
				action = 'store_true',
				default = False,
				help = 'only count lines')
parser.add_option('-f', '--file',
				dest = 'files',
				action = 'store',
				type = 'string',
				help = 'only count lines')
args = [ '-f', 'foo.txt', '-l', '40']
options, args = parser.parse_args(args)

#data = sys.stdin.read()
#chars = len(data)
#words = len(data.split())
#lines = data.count('\n')
#
#if not (options.chars or options.words or options.lines):
#	options.chars, options.words, options.lines = True, True, True
#
if options.chars:
	print options.chars,
if options.words:
	print options.words,
if options.lines:
	print options.lines,
if options.files:
	print options.files
