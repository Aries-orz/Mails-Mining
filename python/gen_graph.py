import json
import re
import string

def get_name(s):
    identify = string.maketrans('', '')
    delEStr = string.punctuation
    name = str(s).strip()
    if '<' in name:
        p = re.compile(r'<.*?>')
        name = re.sub(p,'',name).strip()
    if '[' in name:
        p = re.compile(r'\[.*?\]')
        name = re.sub(p,'',name).strip()
    if '(' in name:
        p1 = re.compile(r'\(.*?\)')
        name = re.sub(p1,'',name).strip()
    if '@' in name:
        name = name.split('@')[0]
    if '.web' in name:
        name = name.replace('.web','')
    if '.' in name:
        name = name.replace('.',' ')
    name = name.translate(identify, delEStr) 
    name = name.title()
    return name

file_in = open('graph.json','r')
file_out = open('relation.json','w')
data = json.load(file_in)
nodes = []
nodes1 = []
edges = []

dict = {}
dict1 = {}
for item, value in data.items():
    item = get_name(item)
    post = len(value)
    if item not in dict:
        dict[item] = post
    else:
        dict[item] = dict[item] + post
    for va in value:
        va = get_name(va)
        if va not in dict:
            dict[va] = 1
        else:
            dict[va] = dict[va] + 1
dict = sorted(dict.iteritems(),key = lambda asd:asd[1], reverse = True)[:20]
for it in dict:
    node = {"name":it[0],"value":it[1]}
    nodes.append(node)
    nodes1.append(it[0])
print 'done 1'

for item, value in data.items():
    if get_name(item) in nodes1:
        for va in value:
            if get_name(va) in nodes1:
                edge =get_name(item)+'|'+get_name(va)
                if edge not in dict1:
                    dict1[edge] = 1
                else:
                    dict1[edge] = dict1[edge]+1

for key,value in dict1.items():
    edge = {"source":nodes1.index(key.split('|')[0]),"target":nodes1.index(key.split('|')[1]),"width":value}
    edges.append(edge)
print 'done 2'


relation = {"nodes":nodes,"edges":edges}

file_out.write(json.dumps(relation, indent=4))

file_in.close()
file_out.close()
