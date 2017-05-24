#!/usr/bin/python

from subprocess import Popen,PIPE
import urllib2,urllib
import pickle

def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return data

def getDmi():
    p = Popen(['dmidecode'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return data

def getHostname(file):
    with open(file) as fd:
        for line in fd:
            if line.startswith('HOSTNAME'):
                hostname = line.split('=')[1].strip()
                break
    return {'hostname':hostname}

def getOSver(file):
    with open(file) as fd:
        for line in fd:
            osver = line.strip()
            break
    return {'osver':osver}

def getCpu(file):
    num = 0
    with open(file) as fd:
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].strip().split()
                cpu_model = cpu_model[0] + ' ' + cpu_model[-1]
    return {'cpu_model': cpu_model, 'cpu_num': num}

def getMemory(file):
    with open(file) as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                memory = int(line.split()[1].strip())
                memory = '%.2f M' %(memory/1024.0)
    return {'memory': memory}

def parseData(data):
    new_line = ''
    parsed_data = []
    data = [i for i in data.split('\n') if i]
    for line in data:
        if line[0].strip():
            parsed_data.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    parsed_data.append(new_line)
    return [i for i in parsed_data if i]

def parseIfconfig(parsed_data):
    dic = {}
    parsed_data = [i for i in parsed_data if not i.startswith('lo')]
    for lines in parsed_data:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
        macaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        break
    dic['ip'] = ipaddr
    return dic

def parseDmi(parsed_data):
    dic = {}
    parsed_data = [i for i in parsed_data if i.startswith('System Information')]
    parsed_data = [i for i in parsed_data[0].split('\n')[1:] if i]
    dmi_dic = dict([i.strip().split(': ') for i in parsed_data])
    dic['vendor'] = dmi_dic['Manufacturer']
    dic['product'] = dmi_dic['Product Name']
    dic['sn'] = dmi_dic['Serial Number'][:15]
    return dic

if __name__ == '__main__':
    dic = {}
    data_ip = getIfconfig()
    parsed_data_ip = parseData(data_ip)
    ip =  parseIfconfig(parsed_data_ip)
    data_dmi = getDmi()
    parsed_data_dmi = parseData(data_dmi)
    dmi = parseDmi(parsed_data_dmi)
    hostname = getHostname('/etc/sysconfig/network')
    osver = getOSver('/etc/issue')
    cpu = getCpu('/proc/cpuinfo')
    memory = getMemory('/proc/meminfo')
    dic.update(ip)
    dic.update(dmi)
    dic.update(hostname)
    dic.update(osver)
    dic.update(cpu)
    dic.update(memory)
    #data = urllib.urlencode(dic)
    data = pickle.dumps(dic)
    req = req = urllib2.urlopen('http://192.168.14.131:8000/hostinfo/collect/', data)
    print req.read()
