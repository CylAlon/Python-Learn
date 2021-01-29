
"""
    接收用户输入文件名
    规划备份文件名
    备份文件写入数据
"""
# 接收
old_name=input("输入你的文件名：")
print(old_name)

# 提取后缀
index=old_name.rfind('.')

hz=old_name[index:]
new_name=old_name[:index]+'[备份]'+hz
print(new_name)

fr=open(old_name,'r')
fw=open(new_name,'w')
while True:
    con=fr.read()
    print(con)
    if len(con)==0:
        break
    fw.write(con)
fr.close()
fw.close()

"""
rename()
remove()
mkdir()
getcwd()
listdir()
rmdir()
"""






