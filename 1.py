import glob
import os

filesA = glob.glob('A/*')
for file in filesA:
    baseName = os.path.basename(file)
    contentA = {} # 记录A的内容
    with open(file, 'r', encoding = 'utf8') as f: # 读取文件A
        lines = f.readlines()
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            contentA[line] = True
    contentB = {}  # 记录B的内容
    contentC = []  # 记录A有B没有的内容
    contentD = []  # 记录B有A没有的内容
    with open('B/' + baseName, 'r', encoding = 'utf8') as f: # 读取文件B
        lines = f.readlines()
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            contentB[line] = True
            if line not in contentA:
                contentD.append(line)
    for line in contentA:
        if line not in contentB:
            contentC.append(line)
    with open('C/' + baseName, 'w', encoding = 'utf8') as f: # 写入文件C
        for line in contentC:
            f.write(line + '\n')
    with open('D/' + baseName, 'w', encoding = 'utf8') as f: # 写入文件D
        for line in contentD:
            f.write(line + '\n')
