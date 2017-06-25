#!/usr/bin/env python

import MySQLdb

def book_list():
    db = MySQLdb.connect(user='root', db='test', passwd='vagrant', host='localhost')
    cursor = db.cursor()
    cursor.execute('select * from book')
    for name in cursor.fetchall():
        print name
        
    db.close()
    
if __name__ == '__main__':
    book_list()
    