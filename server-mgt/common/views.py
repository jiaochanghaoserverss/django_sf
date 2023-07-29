# 调用tornado库
from tornado.web import RequestHandler
import logging

from conf.configs import FILE_PATH


# Hello处理器
class BaseRequestHandler(RequestHandler):
    # 日志方法
    def log(self, msg):  # msg为日志输出的信息
        logger = logging.getLogger('logger')
        logger.setLevel(level=logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

        # 规定日志保存的路径
        file_handler = logging.FileHandler(FILE_PATH)
        file_handler.setLevel(level=logging.INFO)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        logger.info(msg)

    # on_finish方法重写
    def on_finish(self):
        # 获取请求路径，请求方法，请求头，拼接成字符串，传入log方法，作为日志所保存的内容
        msg = str(self.request.method) + "  " + str(self.request.path)
        # 调用log方法
        self.log(msg)
