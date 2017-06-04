#!/usr/bin/python

from subprocess import Popen,PIPE

def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return data

def getDmi():
    p = Popen(['dmidecode'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return data

def parseData(data):
    new_line = ''
    parse_data = []
    data = [i for i in data.split('\n') if i]
    for line in data:
        if line[0].strip():
            parse_data.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    parse_data.append(new_line)
    return [i for i in parse_data if i]

def parseIfconfig(data):
    parse_data = [i for i in parse_data if i and i.startswith('lo')]
    for lines in parse_data:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
        macaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        break
    dic['ip'] = ipaddr
    return dic

def parseDmi(data):
    dic = {}
    data = [i for i in data if i.startswith('System Information')]
    data = [i for i in data[0].split('\n')[1:] if i]
    dmi_dic = dict([i.strip.split(': ') for i in data])
    dic['vendor'] = dmi_dic['Manufacturer']
    dic['product'] = dmi_dic['Product Name']
    dic['sn'] = dmi_dic['Serial Number']
    return dic

if __name__ == '__main__':
    dic_finally = {}
    
