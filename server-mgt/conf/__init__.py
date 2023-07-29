# _*_ coding: utf-8_*_


import tornado.web  # WEB框架
import tornado.httpserver  # http服务
import tornado.ioloop  # 输入/输出事件循环
import tornado.options  # 配置工具
from tornado.options import options, define  # 选项, 定义配置

from conf.urls import urls  # 导入路由
from conf.configs import SETTINGS  # 导入配置

# 定义该服务端口
define("port", default=8000, type=int, help="运行端口")


# 自定义应用
class CustomApplication(tornado.web.Application):
    # 重写__init__初始化构造方法
    def __init__(self):
        # 路由规则
        handlers = urls
        # 指定配置信息
        settings = SETTINGS
        # 调用父类__init__方法  传入上面参数
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


# 2.自定义服务
def create_server():
    # 允许在命令行启动
    tornado.options.parse_command_line()
    # 创建http服务:
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication()
    )
    # 绑定监听端口
    http_server.listen(options.port)
    # 启动输入输出事件循环
    tornado.ioloop.IOLoop.current().start()
