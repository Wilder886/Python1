#用pprint读取打印json
import  json
import pprint
import re
class Read():
    def read_json(self):
        return json.load(open('F:\Python\\1ZoneUncontrolled_win_test.epJSON',encoding='utf-8'))['Building']
#[打印的条目的名字]
read=Read()
pprint.pprint((read.read_json()))
#读取完成


#尚且不知道idf换json是否能有用
#尝试修改json文件中的数据
lines=[]
with open('F:\Python\\1ZoneUncontrolled_win_test.epJSON','r') as f:
    for line in f:
        lines.append(line)#将json内容置入lines中
new_lines=lines[:9]
new_lines.append(lines[7].replace('0.004','temperature_convergence_tolerance_value'))
new_lines.extend(lines[8:])

with open('F:\Python\\1ZoneUncontrolled_win_test.epJSON','w') as f:
     for line in  new_lines:
         f.write(line)
pprint.pprint((read.read_json()))
#这好像没啥用啊......

#开始尝试调用energyplus 去demo5吧


