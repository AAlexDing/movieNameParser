import re

from sqlalchemy import true
from common import parse
'''
name = '吸血夜-vampyres..亿万同人字幕组&橘里橘气译制组'
patterns = '(?:(?:- ?(?:[^-]+(?:-={[^-]+-?$)?))$|(?:[\[〖『「《【]?[a-zA-Z&\u4e00-\u9fa5]+(?:译制组|压制组|字幕组|原创组|小组|出品|论坛|龙网)[\]】〗』」》·]?))'
match = re.findall(patterns, name, re.I)  
print(match)
'''


f = open('.\\doc\\filename.txt', 'r',encoding='utf-8-sig') 
lines = f.readlines()
f.close()
for name in lines:
    name = name.replace('\n','')
    print(name)
    result = parse(name)
    print(result)
    if result.get('excess'):
        input()

'''
name = '[现代启示录].Apocalypse.Now.2001.Redux.BluRay.720p.x264.AC3-CMCT.mkv'
print(parse(name))
!!!!!DTS-X DTS????
'''

'''



'''


