# 导入包
import yagmail

# 创建一个对象

ya_obj = yagmail.SMTP(user="960947610@qq.com", password="ccscrqszqbcobdch", host="smtp.qq.com")
content = "你好"
ya_obj.send("1035557153@qq.com", "测试一一下", content)

print("发送成功")
