import pymysql
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()


global LOGIN_FLAG   # 登陆标志


class_state=[0,1,2,3] # 上课状态 0 出勤  1 请假 2 迟到 3 旷课






