import logging.handlers
import os
from config import BASE_PATH


class GetLog:
    log = None
    file_path = BASE_PATH + os.sep +"log"+os.sep+"hmtq.log"
    @classmethod
    def get_log(cls):
        if cls.log is None:
            # 获取日志器
            cls.log = logging.getLogger()
            # 设置 日志器总级别
            cls.log.setLevel(logging.INFO)
            # 获取 处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=GetLog.file_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取 格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.log.addHandler(th)
        # 返回 日志器
        return cls.log

if __name__ == '__main__':
    GetLog.get_log().info("信息级别调试！")
    GetLog.get_log().error("错误级别调试！")