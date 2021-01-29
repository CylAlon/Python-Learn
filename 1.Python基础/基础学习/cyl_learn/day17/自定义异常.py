class shoError(Exception):
    def __init__(self, length, mins):
        self.length = length
        self.mins = mins

    def __str__(self):
        return f"你输入的长度所示{self.length},最段长度为{self.mins}"


def main():
    try:
        con = input("请输入密码：")
        if len(con) < 3:
            raise shoError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print("密码已经输入完成")


main()
