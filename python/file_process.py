#-*- coding:utf-8 -*-
import os,glob
import time,datetime
import re
import json

#获取目录下所有邮件文件路径
def get_file_list(dir_path, extension_list):
    os.chdir(dir_path)
    file_list = []
    for extension in extension_list:
        extension = '*.' + extension
        file_list += [os.path.realpath(e) for e in glob.glob(extension)] 
    return file_list

#时间格式转换
def timecov(timestr):
    time_original = timestr.strip()
    time_format = datetime.datetime.strptime(time_original, '%A, %B %d, %Y %I:%M %p')
    time_format = time_format.strftime('%Y%m')
    return time_format

dir_path = 'E:\mail\Redacted'
extension_list = ['txt']
all_file = get_file_list(dir_path, extension_list)              #邮件文件路径列表

send = {}
receive = {}
graph = {}

for files in all_file:
    p = re.compile(r'From:.*?Subject:.*?\n',re.DOTALL)
    with open(files, 'r') as f:
        text = unicode(f.read(),errors='ignore')
        for m in p.findall(text):
            info = m.strip().split('\n')
            data = sorted(info)
            if 'From' in data[0] and len(data)>=2:
                cc_data = []
                from_data = data[0]
                time_data = data[1]
            elif 'Cc' in data[0] and len(data)>=3:
                cc_data = data[0]
                from_data = data[1]
                time_data = data[2]
            to_data = data[-1]
            try:
                from_name = from_data.split('m:')[1].strip()
                mail_time = timecov(time_data.split('t:')[1].strip())
                if to_data:
                    if ';' in to_data.split(':')[1].strip():
                        to_name = to_data.split('o:')[1].strip().split(';')
                    else:
                        to_name = [to_data.split('o:')[1].strip()]
                else:
                    to_name = []
                if cc_data:
                    if ';' in cc_data.split(':')[1].strip():
                        cc_name = cc_data.split(':')[1].strip().split(';')
                    else:
                        cc_name = [cc_data.split(':')[1].strip()]
                else:
                    cc_name = []

                if from_name=='Jeb Bush':
                    if mail_time not in send:
                        send[mail_time]=1
                    else:
                        send[mail_time]=send[mail_time]+1
                    for name in to_name:
                        if 'Jeb Bush' not in graph:
                            graph['Jeb Bush']=[name]
                        else:
                            graph['Jeb Bush'].append(name)
                    if cc_name:
                        for name in cc_name:
                            if 'Jeb Bush' not in graph:
                                graph['Jeb Bush']=[name]
                            else:
                                graph['Jeb Bush'].append(name)
                elif 'Jeb Bush' in to_name:
                    if mail_time not in receive:
                        receive[mail_time]=1
                    else:
                        receive[mail_time]=receive[mail_time]+1
                    for name in to_name:
                        if from_name not in graph:
                            graph[from_name]=[name]
                        else:
                            graph[from_name].append(name)
                    if cc_name:
                        for name in cc_name:
                            if from_name not in graph:
                                graph[from_name]=[name]
                            else:
                                graph[from_name].append(name)
                elif 'Jeb Bush' in cc_name:
                    if mail_time not in receive:
                        receive[mail_time]=1
                    else:
                        receive[mail_time]=receive[mail_time]+1
                    for name in to_name:
                        if from_name not in graph:
                            graph[from_name]=[name]
                        else:
                            graph[from_name].append(name)
                    for name in cc_name:
                        if from_name not in graph:
                            graph[from_name]=[name]
                        else:
                            graph[from_name].append(name)
            except:
                continue

send = sorted(send.iteritems(), key=lambda d:d[0], reverse = False)
receive = sorted(receive.iteritems(), key=lambda d:d[0], reverse = False)

with open('E:\\mail\\data\\send.json','w') as f1,open('E:\\mail\\data\\receive.json','w') as f2,open('E:\\mail\\data\\graph.json','w') as f3:
    f1.write(json.dumps(send, indent =4))
    f2.write(json.dumps(receive, indent = 4))
    f3.write(json.dumps(graph,indent = 4))

