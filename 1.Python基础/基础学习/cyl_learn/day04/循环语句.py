# while循环
a = 0
while a < 10:
    a += 1
    if a >= 5:
        break  # 推出后面全部
    elif a == 3:
        continue  # 退出当前
    else:
        print(a)

# for循环
b = "cqust"
for i in b:
    if i == 'q':
        continue
    elif i == 's':
        break
    else:
        print(i)
for i in range(5):
    print(i, end="\t")

# while 和else 配合
c=9
while c<10:
    c+=1
   # break  # break 后 以及  else不执行 非正常结束
    continue  # 正常结束 else要执行
    print("c<10")

else:  #不满住条件
    print("c>=10-------------------------------")

# for else结合
for i in range(10):
    print(i)
else:  # 循环结束后执行的
    print("结束循环")

