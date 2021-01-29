# 导入psutil模块
import psutil
import datetime
# 获取cpu信息

# 获取cpu的核心数
print(psutil.cpu_count())
# 获取物理的核心数
print(psutil.cpu_count(logical=False))

# 获取cpu的利用率
print(psutil.cpu_percent(interval=0.5)) # interval 0.5s获取 刷新频率
print(psutil.cpu_percent(interval=0.5,percpu=True)) # percpu 获取每个核心的使用率

# 获取内存信息
# 内存的总体信息
print(psutil.virtual_memory())
# 内存的使用率
print(psutil.virtual_memory().percent)

# 获取硬盘信息
# 获取分区信息
print(psutil.disk_partitions())
# 获取指定目录的磁盘信息
print(psutil.disk_usage("/"))
# 获取使用率
print(psutil.disk_usage("/").percent)

# 获取到网络信息
# 获取到的数据包大小
print(psutil.net_io_counters().bytes_sent)
print(psutil.net_io_counters().bytes_recv)
# 获取开机时间
print(psutil.boot_time())
date=datetime.datetime.fromtimestamp(psutil.boot_time())
print(date)





























