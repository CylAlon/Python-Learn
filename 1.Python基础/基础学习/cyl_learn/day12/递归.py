
# 应用 3以内数字累加和

# 3以内的数字累加 = 3 + 2 的累加
# 2以内数字累加 = 2 + 1一类的数字累加
# 1以内数字累加 = 1 # 出口


def leijia(num):
    if num==1:
        return 1
    return num+leijia(num-1)
"""
    leijia(3)
        3+leijia(2)-->3
            2+leijia(1)-->1
                return 1
"""
print(leijia(3))





























