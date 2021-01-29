def diannao():
    # 导入模块
    import psutil
    import datetime
    #  定义保存cpu使用率变量
    cpu_per = psutil.cpu_percent(interval=0.5)
    # 定义内存使用率变量
    memory_info = psutil.virtual_memory().percent
    # 定义u硬盘信息
    disk_info = psutil.disk_usage("/").percent
    # 定义变量保网络的信息
    net_info = psutil.net_io_counters().bytes_recv
    # 拼接字符串显示
    print(f"cpu使用率：{cpu_per}\n"
          f"内存使用情况：{memory_info}\n"
          f"硬盘使用u硬盘使用情况ian：{disk_info}\n"
          f"网络使用情况：{net_info}")
    dat = datetime.datetime.fromtimestamp(psutil.boot_time())
    print(f"时间：{dat}")
    # 保存到日志文件
    lo = open("log.txt", "w")
    lo.write(str(dat))
    lo.close()


if __name__ == "__main__":
    while True:
        diannao()
