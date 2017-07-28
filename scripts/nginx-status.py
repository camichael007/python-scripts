#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 9:21
# @Author  : daozai
# @File    : nginx-status.py
# @Software: PyCharm Community Edition

import requests
import sys
import time
import commands
import re

def get_stream_logger(name):
    """获取一个输出到文件的 logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    
    record = logging.FileHandler("/tmp/nginx_cron.log")
    record.setFormatter(formatter)
    record.setLevel(logging.INFO)
    logger.addHandler(record)
    
    return logger

def getJson(url):
    try:
        res = requests.get(url)
        source_data = res.json()
    except ValueError:
        print "No JSON object could be decoded"
    return source_data

def getDomain(zone_name):
    domains = []
    for i in source_data[zone_name]:
        if re.match(r".+?.[(com)(org)]$",i):
            domains.append(i.encode('utf-8'))
    return domains

def getPayload(domains):
    payload = []
    for domain in domains:
        statistic = []
        for metric in source_data['serverZones'][domain]['responses']:
            if re.match(r".+?xx$",metric):
                statistic.append(getTemplate(domain, metric, source_data['serverZones'][domain]['responses'][metric], ip))
        payload.append(statistic)
    return payload

def getTemplate(domain,metirc,value,ip):
    template = {
        "endpoint": str(ip),
        "metric": str(metirc),
        "timestamp": int(time.time()),
        "step": 60,
        "value": value,
        "counterType": "GAUGE",
        "tags": "domain=" + str(domain),
    }
    return template
    
if __name__ == "__main__":
    ip_cmd = "/sbin/ifconfig | grep inet | grep -v inet6 | grep -v '127.0.0.1' | grep '192.168' | awk '{print $2}' | awk -F ':' '{print $2}'"
    ip = commands.getoutput(ip_cmd)
    url = "http://test.juanpi.com/status/format/json"
    source_data = getJson(url)
    zone_name = "serverZones"
    domains = getDomain(zone_name)
    payload = getPayload(domains)
    print payload
